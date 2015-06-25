'''
Created on Jun 8, 2015

@author: abhijit kalamkar
'''

PROFILE_BUCKET = '/dovetail-profiles/'
# MEDIA_MAX_AGE = 30 * 24 * 60 * 60
MEDIA_MAX_AGE = 60 * 60

APNS_DEV = ('gateway.sandbox.push.apple.com', 2195)
APNS = ('gateway.push.apple.com', 2195)
GCM_URL = 'https://android.googleapis.com/gcm/send'

GCM_API_KEY = 'AIzaSyBOrPebHVw-4vTWjcgXOVPQUjAOajCeXEw'

CERT = """-----BEGIN CERTIFICATE-----
MIIFkjCCBHqgAwIBAgIIP8Ou/DQ2r1wwDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV
BAYTAlVTMRMwEQYDVQQKDApBcHBsZSBJbmMuMSwwKgYDVQQLDCNBcHBsZSBXb3Js
ZHdpZGUgRGV2ZWxvcGVyIFJlbGF0aW9uczFEMEIGA1UEAww7QXBwbGUgV29ybGR3
aWRlIERldmVsb3BlciBSZWxhdGlvbnMgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkw
HhcNMTQwMjIxMDEwNzIwWhcNMTUwMjIxMDEwNzIwWjCBkTEnMCUGCgmSJomT8ixk
AQEMF2NvbS50ZWRkeXRhYi5Cb29rUmVhZGVyMUQwQgYDVQQDDDtBcHBsZSBQcm9k
dWN0aW9uIElPUyBQdXNoIFNlcnZpY2VzOiBjb20udGVkZHl0YWIuQm9va1JlYWRl
cjETMBEGA1UECwwKOTVFR0oyNTJOSjELMAkGA1UEBhMCVVMwggEiMA0GCSqGSIb3
DQEBAQUAA4IBDwAwggEKAoIBAQDOHCSsOyhUsp8Twvt3/X3C/UrVJtsuSfHZ0IXq
iqhVCsKgsDo5ipj1UNOhCt17nLdFU+g+kOY3su4LlrQcTVKfE1zO915u8NOhWWpU
8HTjNYoREbCKeZnjff5e57flnJqyHJP6hRzai77WnKSQouNjENZOaCX7vG8rgw/b
NUC93UsnqUZuJEfQpctr+VZqmxsvBSb0c0xf9sN/luOIKGik8eiyU6mEEGEdnIIm
lW3EL0/D+s0lsH6LzsoL/OGjR8ROCzRchuS4gFM3T+/0SDRXr4HfDHSKzC5T3yV4
2r3EK8hofN1PSOmFX86m0mQzYzKO1eLYKZ4H1vGmQvVMZNNLAgMBAAGjggHlMIIB
4TAdBgNVHQ4EFgQULXa7CfQ50Wqtc/hdwNa+45UnfPgwCQYDVR0TBAIwADAfBgNV
HSMEGDAWgBSIJxcJqbYYYIvs67r2R1nFUlSjtzCCAQ8GA1UdIASCAQYwggECMIH/
BgkqhkiG92NkBQEwgfEwgcMGCCsGAQUFBwICMIG2DIGzUmVsaWFuY2Ugb24gdGhp
cyBjZXJ0aWZpY2F0ZSBieSBhbnkgcGFydHkgYXNzdW1lcyBhY2NlcHRhbmNlIG9m
IHRoZSB0aGVuIGFwcGxpY2FibGUgc3RhbmRhcmQgdGVybXMgYW5kIGNvbmRpdGlv
bnMgb2YgdXNlLCBjZXJ0aWZpY2F0ZSBwb2xpY3kgYW5kIGNlcnRpZmljYXRpb24g
cHJhY3RpY2Ugc3RhdGVtZW50cy4wKQYIKwYBBQUHAgEWHWh0dHA6Ly93d3cuYXBw
bGUuY29tL2FwcGxlY2EvME0GA1UdHwRGMEQwQqBAoD6GPGh0dHA6Ly9kZXZlbG9w
ZXIuYXBwbGUuY29tL2NlcnRpZmljYXRpb25hdXRob3JpdHkvd3dkcmNhLmNybDAL
BgNVHQ8EBAMCB4AwEwYDVR0lBAwwCgYIKwYBBQUHAwIwEAYKKoZIhvdjZAYDAgQC
BQAwDQYJKoZIhvcNAQEFBQADggEBAJNeVol6mtpOoVADNUSTw5TA+YXMnEheDn7H
Np4uRRXA2M3fAXb7k3r4JJ5MJW8/IvjFct3lCEI6nqG+IhJ1q2Oj7rYDEwz2xl1U
NuKrR6NDwl6fxLkdt89LOqv5TWR3YiZ5VnT8vk9Z+7aX2TpotAsO1wpwPwlKNWW4
ZaC0jK4qQAqjIQa/rWiXGe22yCr/ItZotr+WUNDyo7J8gi6jSQTKkYOEqSH2zGdd
m95HuVCWFGZ2DOlIiqU3uc25ATovRrkDKR/WinpO0bI5N6hRFdooDsTHztdGKTpd
OOBwUphHGL3pbHaKsm+rRdPTZ6RbSF9U6CQtJGSgUiuNwUPnVPg=
-----END CERTIFICATE-----"""

KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAzhwkrDsoVLKfE8L7d/19wv1K1SbbLknx2dCF6oqoVQrCoLA6
OYqY9VDToQrde5y3RVPoPpDmN7LuC5a0HE1SnxNczvdebvDToVlqVPB04zWKERGw
inmZ433+Xue35ZyashyT+oUc2ou+1pykkKLjYxDWTmgl+7xvK4MP2zVAvd1LJ6lG
biRH0KXLa/lWapsbLwUm9HNMX/bDf5bjiChopPHoslOphBBhHZyCJpVtxC9Pw/rN
JbB+i87KC/zho0fETgs0XIbkuIBTN0/v9Eg0V6+B3wx0iswuU98leNq9xCvIaHzd
T0jphV/OptJkM2MyjtXi2CmeB9bxpkL1TGTTSwIDAQABAoIBAQCthaYeVmO7AvLI
iWR6/bBOZD8HOwJWcyypS1QjRP85Majv7c3nOddS2OyC7YnQEv184YpqekVH6V1d
5k/WcAa6JGwDVuFrF1ekxImv3w0ZaK7HdhQiUQQNMbrhHcaGChV3FHZE+KJ1ICfX
uOMXXfuAIOG7+xTXXipeAKZtz+SkstIu+l0z9TBeSaQtfc6PjytU46buMSr3a8Cz
7HpiX3P+SY0p4FQdI8ahfgrHjddd5h2qgixpspHu/Gk//THEzw3RLZGFOB4VeTNZ
tHERLXmXOcvsY4RIjArlWutul1SUpmJ6rjuubwab9zjH8tCkngN5G6xAfSShLpEm
GWz/ejORAoGBAOxSxykSUiyK9l8U1g9w2/RdhOUTfUULaZubQHbfHr3MDg74XnrM
cqsNtbbqueYUAbgQnwHLbZTrXVOfNn/1mZToVTgInH4x/9mIsR7v2j9GLXjvBxr6
740nUTySFXXWCiwWEm5V0IeLM4ngQ2hvMo+odiMY3sZZO9s38P9fNml5AoGBAN9F
Xht98vuGTH8JwD2oPapDXIEG5Ax6Su1PwcrPu/tW4XybzmAZ1gxpb9s/YYI+ByY8
igQnRS7kNwTQNnKFVWxW+4ASHaxetILkfA04Yh9OQ5xPZOvu0W+2TRHeTKtFzgY7
5BUPyykvs+/j15HzETquN9JvftvKmMHFN0ptOXXjAoGBAIGyAElDG8QEU6fk6IG6
34vh0zBhHMvKsp/KeXuDgfyJw2Fl33wnPfswX/zOH03sxvC8dndmrHIhJavh4egh
4rK9Ox+wYipDyHUbNpGS8sTs/8Gx9MVS2CswW74RMiPkXtrJFj5lbDcnJxbQ9E2Z
UTdULdmfKYvTpyztK58LIvKJAoGBANaOb7AVqeHiHjLaqP3XZmLvVr67Y31GLCi/
Q2jlli0jQY8gnwMk8Nh+njpgPxENEIvDE5KINmiocOLUP+5viTaSpB9fyVoyrF84
uKlvrIOPD1Pvy/kaR/OFiayJJr5UV3cQKM/AnKhYqh72odskbUMp1oUIFi2bFI7p
OYfxTI2nAoGAYr85MNzAcfuPCZrv/4tnSQO3B3pdUcBBtl7nXNXRa40KgjfU4G1T
Q9q/7Mfy0Bkdvvpxe2dvAqDVcXes0HZC9VsIw19nAT0GYKdnwhRCaqHvW8lI45+e
1EqR/Cd/tBpXziHJESlr7n8AvVYR5GdYiVgwqHm7PFyUj3l0cpwq4Hc=
-----END RSA PRIVATE KEY-----"""

CERT_DEV = """-----BEGIN CERTIFICATE-----
MIIFhTCCBG2gAwIBAgIICYAJbwt6jhgwDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV
BAYTAlVTMRMwEQYDVQQKDApBcHBsZSBJbmMuMSwwKgYDVQQLDCNBcHBsZSBXb3Js
ZHdpZGUgRGV2ZWxvcGVyIFJlbGF0aW9uczFEMEIGA1UEAww7QXBwbGUgV29ybGR3
aWRlIERldmVsb3BlciBSZWxhdGlvbnMgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkw
HhcNMTUwNjE3MjExOTI4WhcNMTYwNjE2MjExOTI4WjCBhDEgMB4GCgmSJomT8ixk
AQEMEERULkRvdmVUYWlsQXBwbGUxPjA8BgNVBAMMNUFwcGxlIERldmVsb3BtZW50
IElPUyBQdXNoIFNlcnZpY2VzOiBEVC5Eb3ZlVGFpbEFwcGxlMRMwEQYDVQQLDAo5
NDRFU0M2M0JTMQswCQYDVQQGEwJVUzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCC
AQoCggEBAMn+nmyNhkjejjGbciwC2ACiDCSPIIdD3q8+myYU2/dPLUFtfRUXOcRr
Rnl8EA+46FHyPqAaLg4lGYlkgE9sujAJ984iPFB1BL2CuBu+eLhT+2wf0uNN2CuR
5yiKtyCtHl9FK9tOlyllwE1BhG6Kzlq7X9xQXyS4v6AMnpdHrLdZbJC+h83eniuV
5dZUBd04hmYAQZ3bg6lhSekiUpzFFD264SBGN/7f/E20wpiBO0MKNRApFREeLslH
ay/FXrk+Jjk8EeMM1wYEy9+mvpOXXfxjYbmLFx8RPd3i5XzFBUffR5bEZlIac3OX
BWwxKbLV5C0RXjLfXbOpaKYRjWB8UNsCAwEAAaOCAeUwggHhMB0GA1UdDgQWBBQK
3aga4TieNcT29kDCvZH95ZXxdTAJBgNVHRMEAjAAMB8GA1UdIwQYMBaAFIgnFwmp
thhgi+zruvZHWcVSVKO3MIIBDwYDVR0gBIIBBjCCAQIwgf8GCSqGSIb3Y2QFATCB
8TCBwwYIKwYBBQUHAgIwgbYMgbNSZWxpYW5jZSBvbiB0aGlzIGNlcnRpZmljYXRl
IGJ5IGFueSBwYXJ0eSBhc3N1bWVzIGFjY2VwdGFuY2Ugb2YgdGhlIHRoZW4gYXBw
bGljYWJsZSBzdGFuZGFyZCB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZiB1c2UsIGNl
cnRpZmljYXRlIHBvbGljeSBhbmQgY2VydGlmaWNhdGlvbiBwcmFjdGljZSBzdGF0
ZW1lbnRzLjApBggrBgEFBQcCARYdaHR0cDovL3d3dy5hcHBsZS5jb20vYXBwbGVj
YS8wTQYDVR0fBEYwRDBCoECgPoY8aHR0cDovL2RldmVsb3Blci5hcHBsZS5jb20v
Y2VydGlmaWNhdGlvbmF1dGhvcml0eS93d2RyY2EuY3JsMAsGA1UdDwQEAwIHgDAT
BgNVHSUEDDAKBggrBgEFBQcDAjAQBgoqhkiG92NkBgMBBAIFADANBgkqhkiG9w0B
AQUFAAOCAQEAXga3p8BsvPlI07i5QUPqYXmGoCr+CBKv5iDCnYmdkhf8+x0DU13u
Xxt6ZUxTJToAtl6knM2/ymvFVPcKUa1Nq9l9yWtZw/j684avNnl2tokPQpxhX5yh
pnRHQD5ROQ2vSDTRnPnb70ZUH40sVxC3gqzhdIartpz8MqnEk8Ma9l0+3MGGRJ0/
FtaoDrRHFY+wenTfOkGbgFEcnnBs2UbGlNqgbssJrQ3NYLD7JHgcI09wkmUsterD
FXy8t1p9hNaeIzaXFSt9EhpKQ5mCjALwXUt7TK1EjWaSPWL2uXDM59QI1JkqTCwz
w1cUuqgjMcC24raj5b4A5rT+49hhaNYPQQ==
-----END CERTIFICATE-----"""

KEY_DEV = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyf6ebI2GSN6OMZtyLALYAKIMJI8gh0Perz6bJhTb908tQW19
FRc5xGtGeXwQD7joUfI+oBouDiUZiWSAT2y6MAn3ziI8UHUEvYK4G754uFP7bB/S
403YK5HnKIq3IK0eX0Ur206XKWXATUGEborOWrtf3FBfJLi/oAyel0est1lskL6H
zd6eK5Xl1lQF3TiGZgBBnduDqWFJ6SJSnMUUPbrhIEY3/t/8TbTCmIE7Qwo1ECkV
ER4uyUdrL8VeuT4mOTwR4wzXBgTL36a+k5dd/GNhuYsXHxE93eLlfMUFR99HlsRm
Uhpzc5cFbDEpstXkLRFeMt9ds6lophGNYHxQ2wIDAQABAoIBAAcyYjSd6j3oaAqO
bkfxJf8HxwT6cH9BRMrboS1/KsMp+APPwdghhrZf2Bf1+qCExwo8ZkzQAfoRClLh
2Mx7pDqX8FNQ1vNK6AtUf/jFFYoDu/6DN8FPgbczsJe6MYIhiOZ+EWzz5ODdtjdK
cUx695U1/dlcp7coOfOa33+mVxoFLmg7piLS9PsE7FDwAKGcwQ52vUT+xpP7Imrc
XEnulKF3iOiRaFtTLdyWSSr/MKeozK1l/pKUuAhdYIH+DCOE5ByV98nq7CHXjw/u
rLfA33YO4b5qm6qSDDyFGAyjzfRRYZJ+/XFoI8GmlAQOTd1BfwJyiZryrPiWIADv
c693l5kCgYEA7QIrKTqtG0EcQv1N9hmvsosrnNkCAKdzaiqQQJ709fTUl6cfob7E
oFAuL+8ng4bHjulwry5+Bcwtx89TNWJ/WjRVS/GUYHcJN5Hh7+vS2yntjUZBfmf6
ugFavHDybb2U1q3tjOZMK7QRE+8UYJRfpWJtcv6w93Pd4bAFUFcWg1cCgYEA2i4z
EY8EXN/17TI7gGb1n2zHTBpASZXAAKK/VWKxP7fxUa9Gt/AfnVvn9N1HVkkXvpQQ
ODavOPyBzmxV3GwC6971bGIZLxoI9yQ+3tWj7PURUL6tr2Pn1NH4eYxU/l2FxCL+
i1EZsSGcWHoeABhIY2qKCfVUO5JzNJ4t8DDWEB0CgYEAzbC9HpoC1A1s5qKJf5UJ
S63Gmugm+cRZwQDRkpOhyrfBrR/oruouIWeUvhsTMu3M0TW9ivuReZya+rbu4vzp
w7J5eGBfwlxsjmK4MA19QKGhvaMEghzhl35HbhWkACOxQaNO76KK5r7ut1sdVzhN
ze2fSVbK5OcU4KJv6iq6qh8CgYAMuVEFHyAUAoOnF5zcuiRs7b0ZtRY2tGMEJnme
EylfG+0Y5G3tYDWXybpXT2hPoeeel6fyf03stt0jGrJPLoVlGBWcAoSReKU5NIXu
HOt4cDpYSSZ76gmlIbGp9QMn6nBYpenOWiZzbBBgII8LVl8yXQ470nDdIIdTdD4d
mduCCQKBgQCweO0YgWyasmTMs35z+KxjSoimuc19u08exBK6JKSGXxbDIb/3Y6F7
queelgIhlDYHWosIiEbs5G8VJiB+jRmVDdacJoDc/EsaoHfxcUfNSk+sfnMozXIA
jAvevtL4lgs1QPQ2Y2tZ5gHMRCkGjD8WW34WpbIoENZu33rhTyIw7Q==
-----END RSA PRIVATE KEY-----"""
