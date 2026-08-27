import urllib.request, urllib.error, ssl
ctx = ssl.create_default_context()
for h in ['https://api.omniroute.ai/v1/models','https://api.aihubmix.com/v1/models']:
    try:
        req = urllib.request.Request(h)
        r = urllib.request.urlopen(req, timeout=8, context=ctx)
        print(h, '-> OK', r.status)
    except urllib.error.HTTPError as e:
        print(h, '-> REACHABLE', e.code)
    except Exception as e:
        print(h, '-> FAIL', str(e)[:70])
