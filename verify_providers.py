import json, urllib.request, urllib.error, ssl

PATH = '/home/daytona/.openclaw/openclaw.json'
cfg = json.load(open(PATH))
provs = cfg['models']['providers']
ctx = ssl.create_default_context()
for name, p in provs.items():
    url = p.get('baseUrl', '')
    print('PROVIDER:', name, '->', url)
    if not url:
        print('  (no baseUrl)')
        continue
    test = url.rstrip('/') + '/models'
    try:
        req = urllib.request.Request(test)
        r = urllib.request.urlopen(req, timeout=8, context=ctx)
        print('  egress OK status:', r.status)
    except urllib.error.HTTPError as e:
        print('  egress REACHABLE status:', e.code)  # 401/403 still proves reachable
    except Exception as e:
        print('  egress FAIL:', str(e)[:90])
