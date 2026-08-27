import urllib.request, urllib.error, ssl
hosts = ['https://api.deepseek.com/v1/models','https://api.openai.com/v1/models','https://api.anthropic.com/v1/models','https://api.groq.com/openai/v1/models','https://181.208.206.164/']
ctx = ssl.create_default_context()
for h in hosts:
    try:
        req = urllib.request.Request(h)
        r = urllib.request.urlopen(req, timeout=8, context=ctx)
        print(h, '-> OK', r.status)
    except urllib.error.HTTPError as e:
        print(h, '-> REACHABLE', e.code)
    except Exception as e:
        print(h, '-> FAIL', str(e)[:60])
