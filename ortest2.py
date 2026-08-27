import urllib.request, urllib.error, ssl
ctx = ssl.create_default_context()
hosts = ['https://essex-previously-bronze-lone.trycloudflare.com/v1/models',
         'https://trycloudflare.com/']
for h in hosts:
    try:
        req = urllib.request.Request(h)
        r = urllib.request.urlopen(req, timeout=8, context=ctx)
        print(h, '-> OK', r.status)
    except urllib.error.HTTPError as e:
        print(h, '-> REACHABLE', e.code)
    except Exception as e:
        print(h, '-> FAIL', str(e)[:70])
