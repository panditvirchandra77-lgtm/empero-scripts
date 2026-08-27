import json
cfg = json.load(open('/home/daytona/.openclaw/openclaw.json'))
p = cfg['models']['providers']['openrouter']
print('baseUrl:', p.get('baseUrl'))
for m in p.get('models', []):
    print('MODEL:', m.get('id'), '|', m.get('name'))
