import urllib.request, urllib.error, ssl
ctx = ssl.create_default_context()
# test my box's public IP
hosts = [
    'https://45.83.216.16/v1/models',
    'https://45.83.216.16/',
    'https://45.83.216.16/health',
]
for h in hosts:
    try:
        req = urllib.request.Request(h)
        r = urllib.request.urlopen(req, timeout=8, context=ctx)
        print(h, '-> OK', r.status)
    except urllib.error.HTTPError as e:
        print(h, '-> REACHABLE', e.code)
    except Exception as e:
        print(h, '-> FAIL', str(e)[:80])
