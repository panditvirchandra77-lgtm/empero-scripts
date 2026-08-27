import json, urllib.request, urllib.error, ssl
ctx = ssl.create_default_context()
cfg = json.load(open('/home/daytona/.openclaw/openclaw.json'))
key = cfg['models']['providers']['openrouter']['apiKey']
# Test 1: direct openrouter API
body = json.dumps({"model":"deepseek/deepseek-v4-flash","messages":[{"role":"user","content":"say HI"}],"max_tokens":50}).encode()
req = urllib.request.Request('https://openrouter.ai/api/v1/chat/completions', data=body, headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
try:
    r = urllib.request.urlopen(req, timeout=25, context=ctx)
    d = json.loads(r.read().decode())
    print('DIRECT-OR:', d['choices'][0]['message'].get('content') or d['choices'][0].get('message',{}).get('reasoning','')[:80])
except urllib.error.HTTPError as e:
    print('DIRECT-OR ERR:', e.code, e.read().decode()[:200])
except Exception as e:
    print('DIRECT-OR FAIL:', str(e)[:100])
# Test 2: through gw-big gateway (agent endpoint with provider model)
gkey = cfg['gateway']['auth']['token']
body2 = json.dumps({"model":"openrouter/deepseek/deepseek-v4-flash","messages":[{"role":"user","content":"say HI"}],"max_tokens":50}).encode()
req2 = urllib.request.Request('http://localhost:18789/v1/chat/completions', data=body2, headers={'Authorization':'Bearer '+gkey,'Content-Type':'application/json'})
try:
    r2 = urllib.request.urlopen(req2, timeout=40, context=ctx)
    print('GATEWAY:', r2.read().decode()[:300])
except urllib.error.HTTPError as e:
    print('GATEWAY ERR:', e.code, e.read().decode()[:300])
except Exception as e:
    print('GATEWAY FAIL:', str(e)[:100])
