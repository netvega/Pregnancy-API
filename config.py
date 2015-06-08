'''
Created on Jun 8, 2015

@author: abhijit kalamkar
'''

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
MIIFkzCCBHugAwIBAgIId6a+tM6JEGIwDQYJKoZIhvcNAQEFBQAwgZYxCzAJBgNV
BAYTAlVTMRMwEQYDVQQKDApBcHBsZSBJbmMuMSwwKgYDVQQLDCNBcHBsZSBXb3Js
ZHdpZGUgRGV2ZWxvcGVyIFJlbGF0aW9uczFEMEIGA1UEAww7QXBwbGUgV29ybGR3
aWRlIERldmVsb3BlciBSZWxhdGlvbnMgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkw
HhcNMTMwMjE2MTYwMTUwWhcNMTQwMjE2MTYwMTUwWjCBkjEnMCUGCgmSJomT8ixk
AQEMF2NvbS50ZWRkeXRhYi5Cb29rUmVhZGVyMUUwQwYDVQQDDDxBcHBsZSBEZXZl
bG9wbWVudCBJT1MgUHVzaCBTZXJ2aWNlczogY29tLnRlZGR5dGFiLkJvb2tSZWFk
ZXIxEzARBgNVBAsMCjk1RUdKMjUyTkoxCzAJBgNVBAYTAlVTMIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAt646dPTIUqiabsVug3BCxe3xzZ3kuAsjD27j
xIMuJO6G5kF/Ms5JWy+1iUBD1eKcfbGLpEEcEHqmWIPGq8vx6TOSbwquGVSX7FqS
bN+utWDlINi8BdvAmAkdO8UqC3t9dzoLm/nI2iaJKFvHrEFshzIgDcUfgRiGg0SC
O4NX/sUquko3uxwGXjIsyg7y6njKuLRK4Sf9+YpJhDX2mEeOSZOZwOysfvPxfhs2
nUL9XphueDnLuNHQgRo20MCy0MTVNRUBc5ljNINVzeZJeKbJTGzy9lw8i4QMe4sz
fUtFOyUAKUlqhmPaYgRjK0E47y2x9lNaAURSnS9zOCQQImNQdQIDAQABo4IB5TCC
AeEwHQYDVR0OBBYEFIGJmGu/lpYvGGUIbnj6gVH+uNp2MAkGA1UdEwQCMAAwHwYD
VR0jBBgwFoAUiCcXCam2GGCL7Ou69kdZxVJUo7cwggEPBgNVHSAEggEGMIIBAjCB
/wYJKoZIhvdjZAUBMIHxMIHDBggrBgEFBQcCAjCBtgyBs1JlbGlhbmNlIG9uIHRo
aXMgY2VydGlmaWNhdGUgYnkgYW55IHBhcnR5IGFzc3VtZXMgYWNjZXB0YW5jZSBv
ZiB0aGUgdGhlbiBhcHBsaWNhYmxlIHN0YW5kYXJkIHRlcm1zIGFuZCBjb25kaXRp
b25zIG9mIHVzZSwgY2VydGlmaWNhdGUgcG9saWN5IGFuZCBjZXJ0aWZpY2F0aW9u
IHByYWN0aWNlIHN0YXRlbWVudHMuMCkGCCsGAQUFBwIBFh1odHRwOi8vd3d3LmFw
cGxlLmNvbS9hcHBsZWNhLzBNBgNVHR8ERjBEMEKgQKA+hjxodHRwOi8vZGV2ZWxv
cGVyLmFwcGxlLmNvbS9jZXJ0aWZpY2F0aW9uYXV0aG9yaXR5L3d3ZHJjYS5jcmww
CwYDVR0PBAQDAgeAMBMGA1UdJQQMMAoGCCsGAQUFBwMCMBAGCiqGSIb3Y2QGAwEE
AgUAMA0GCSqGSIb3DQEBBQUAA4IBAQCdoNTEFAKCXjZxVmo1cTYvU3RZxT8UNrG/
9hm5eztJCmU+1RKtJXlbH0P9jsFWXRrUmPKLw3YoZbKNCSk1UFoZFpwWxkwtrA+I
ixRWKSkntumb09rDFeyzTYEEAkPLjCFd0B2d7SkVmA2fTFt/plNQsYuONPVzcBA/
/iJReZmeDB7eYAewQqXv43SuIBZmVs74EOYTvWqT0sFQz9MnIWGEyyjZ4+hVa7qu
FBhB0KKjaPxp8fRyk3wCli8j4FY232cxMwAEZ8okhbWmvntFeVGQhBQYueOV1ppS
QiCK0ccNOTD5cDYXjMiTKpGOqfLioQnBn+riSkO8rcgN6XOLxzSj
-----END CERTIFICATE-----"""

KEY_DEV = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAt646dPTIUqiabsVug3BCxe3xzZ3kuAsjD27jxIMuJO6G5kF/
Ms5JWy+1iUBD1eKcfbGLpEEcEHqmWIPGq8vx6TOSbwquGVSX7FqSbN+utWDlINi8
BdvAmAkdO8UqC3t9dzoLm/nI2iaJKFvHrEFshzIgDcUfgRiGg0SCO4NX/sUquko3
uxwGXjIsyg7y6njKuLRK4Sf9+YpJhDX2mEeOSZOZwOysfvPxfhs2nUL9XphueDnL
uNHQgRo20MCy0MTVNRUBc5ljNINVzeZJeKbJTGzy9lw8i4QMe4szfUtFOyUAKUlq
hmPaYgRjK0E47y2x9lNaAURSnS9zOCQQImNQdQIDAQABAoIBAQCAxSN0RPt/f3Ys
/Dqa6QPW8RaY+P2UzTH6KtqBNRoPiC2IlRhQjPA+fjb9jtE/zEu7jtIACCldoC6o
VVHdtO/WdnJNaKZfWb/cUi7fJv27aL+ZhHhkfwgJTjJxaastO5jdEhN7eOUHkwaL
BbT5HTCxo0F3hd+tSH1c35WRlWYGVBCdBgQOkB2KUCQHJLJRvyewdofkrXn88sKz
lU7GCfUDlPGcUkJ+mV/JzgWUfDwaFlEL9tJyjpfzxOZcLiNYaVpNjysXQRarzJx2
6/Hf77j0lVyxBMwDmJlKDis/tRPErbXUVhS02seI1k7VKl1Jf1W6QSxd72hpHyBA
Q11M8UyNAoGBAOvo2YagD20p/H8RBcFr9w6gCqowshVU0Ti+YQa1k0V4GLEBw8Za
5wsY3pOHHJSWwXpcPMgzzfo4/78Iic3nbwN0xjUswRY8b0ZO8pY/cPw5U1yfv6sO
Icv0PZ8zRFfy/t/CROZMYKQdR02GUEwSROxiciOVdydp28tDs4mBmHk/AoGBAMdS
tydCfGuAQaf/t3wWiGm6uDDLLPmHie9YXGu/G2RLuMioIzHEy1Vhdzv/lFKO5Il7
+dAtnUAVhGIOj+ygHemmRI2fya+gGMi1MSGWG1XS05jr6ySNQTHap+L2/M5CS7kI
W4P+MhpOLaH94kkPxBL6mnw5mZ2k2dBPTtLzMnVLAoGAVc0OsKQueCm5KA3s5fh6
ltsmhdfILXH31oeHioUn1zBi6p4VsmMFfUfCTC3r+y8Jl5NMmBQfak6o1bYpSLZP
7hXesSBh6dB5OD0mhfb1BQdkhl+juncdW6ytbOWcidBbWs6xeIF29LmhYVTkh4Zt
gvwbP03xVGhwBHHPLsfvyMkCgYEAs8IFK4LqcojYrYoRD/fCTpf2RQr3JJL38sLd
ls5jBbDElTINi3TPa9Dal2GHgm0b7mHAid6ZUpIVMdmwMta0I2Ovr4nLengH4fqG
tKOLQ3s/GUqqZex+P1fS0P2uQNXJNLY00nUM+mxG+zDcQsfVLMiVSjMoNuPVC+h6
TgTGHMECgYAeEGMbTY3JubbHssEl/JUiHc+4CVm91kZjfRKyTZRVy73lz1j9brmT
FcknK/ZM9C7UtpGpBAOJitQRzeUXvFWGzWKsbN2KcFcg6ueQ8zXQ0oOk+xv4hS6/
1FHCmRNUyH1K8lGAN6EBBQKGkxEgU7+N+kSeWWy397s9oUG2EiYmUQ==
-----END RSA PRIVATE KEY-----"""
