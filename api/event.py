'''
Created on Sep 25, 2014

@author: abhi@dovetail.care (Abhijit Kalamkar)
'''

import datetime
import json
import StringIO
import numpy

from google.appengine.ext import ndb
import webapp2
import matplotlib.pyplot as charts

import api
from datastore import Event
from renderer import get_event_json

class EventAPI(webapp2.RequestHandler):

    def post(self):
        time_millis = self.request.get('time')
        data = self.request.get('data')
        tags = self.request.get('tags')

        try:
            referer = self.request.headers['Referer']
        except:
            referer = ''

        user = api.get_user(self.request)
        if not user and referer.find('/poll') < 0:
            api.write_error(self.response, 400, 'Unknown or missing user')
            return

        if not tags or not time_millis:
            api.write_error(self.response, 400, 'Missing required parameter.')
            return

        tags = tags.lower().split(',')
        time = api.get_time_from_millis(time_millis)
        if user:
            event = Event(parent=user.key, tags=tags, time=time, data=data)
        else:
            event = Event(tags=tags, time=time, data=data)
        event.put_async()

        api.write_message(self.response, 'Successfully added event %s' % (event.key.urlsafe()))

    def get(self):
        start_millis = self.request.get('start_time')
        end_millis = self.request.get('end_time')
        tags = self.request.get('tags')

        user = api.get_user(self.request)
        if not user:
            api.write_error(self.response, 400, 'Unknown or missing user')
            return

        if not tags:
            api.write_error(self.response, 400, 'Missing required parameter, tags.')
            return

        tags = tags.lower().split(',')
        query = get_user_event_query(user, tags, start_millis, end_millis)
        events = []
        for event in query:
            events.append(get_event_json(event))

        api.write_message(self.response, 'success', extra={'events' : events})


class EventChartAPI(webapp2.RequestHandler):
    def get(self):
        tags = self.request.get('tags')
        start_millis = self.request.get('start_time')
        end_millis = self.request.get('end_time')

        if not tags:
            api.write_error(self.response, 400, 'Missing required parameter, tags')
            return

        tags = tags.lower().split(',')
        query = get_user_event_query(None, tags, start_millis, end_millis)
        results = {}
        for event in query:
            try:
                results[event.data] += 1
            except:
                results[event.data] = 1

        if query.count() == 0:
            api.write_error(self.response, 404, 'Not enough data points for chart.')
            return

        output = StringIO.StringIO()
        try:
            charts.clf()
            total = sum(results.values())
            labels = []
            for label in results.keys():
                labels.append(str(results[label] * 100 / total) + '%  ' + label)

            charts.barh(range(len(labels)), results.values(), align='center', color='#E0A6C6',
                                linewidth=0)
            charts.yticks(range(len(labels)), labels, family='sans-serif', ha='left', color='w',
                          weight='normal', size='large', x=0.03)
            charts.xticks([])
            charts.tick_params(left='off', right='off')
            charts.box(False)

            figure = charts.gcf()
            figure.set_size_inches(5, 3)
            figure.savefig(output, dpi=100, orientation='landscape', format='png', transparent=True,
                           frameon=False, bbox_inches='tight', pad_inches=0)
        except:
            pass

        self.response.headers['Content-Type'] = 'image/png'
        # self.response.headers['Cache-Control'] = 'public,max-age=%d' % (config.CHART_MAX_AGE)
        self.response.out.write(output.getvalue())
        output.close()


def get_user_event_query(user, tags, start_millis, end_millis):
    end = api.get_time_from_millis(end_millis)
    if not end:
        end = datetime.datetime.now()

    start = api.get_time_from_millis(start_millis)
    if not start:
        start = api.get_time_from_millis('0')

    if user:
        return Event.query(ndb.AND(Event.tags.IN(tags), Event.time > start, Event.time < end),
                           ancestor=user.key).order(-Event.time)
    else:
        return Event.query(ndb.AND(Event.tags.IN(tags), Event.time > start, Event.time < end)).\
                            order(-Event.time)


def get_average_measurement(user, tags, start_millis, end_millis):
    values = []
    query = get_user_event_query(user, tags, start_millis, end_millis)
    for event in query:
        try:
            measurement = json.loads(event.data)
            values.append(int(measurement['value']))
        except:
            continue

    return numpy.mean(values)

