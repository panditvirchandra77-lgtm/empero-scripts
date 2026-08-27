import json, urllib.request, urllib.error, ssl
ctx = ssl.create_default_context()
cfg = json.load(open('/home/daytona/.openclaw/openclaw.json'))
key = cfg['models']['providers']['openrouter']['apiKey']
print('key prefix:', key[:12], 'len:', len(key))
body = json.dumps({"model":"deepseek/deepseek-v4-flash","messages":[{"role":"user","content":"hi"}],"max_tokens":20}).encode()
req = urllib.request.Request('https://openrouter.ai/api/v1/chat/completions', data=body, headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
try:
    r = urllib.request.urlopen(req, timeout=20, context=ctx)
    print('CHAT:', r.status)
    print(r.read().decode()[:150])
except urllib.error.HTTPError as e:
    print('ERR:', e.code, e.read().decode()[:300])
except Exception as e:
    print('FAIL:', str(e)[:100])
