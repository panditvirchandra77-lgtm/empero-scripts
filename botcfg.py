import json
cfg = json.load(open('/home/daytona/.openclaw/openclaw.json'))
ch = cfg.get('channels', {})
print('channels:', list(ch.keys()))
tg = ch.get('telegram', {})
if tg:
    print('telegram enabled:', tg.get('enabled'), '| botToken:', str(tg.get('botToken',''))[:15]+'...')
adm = cfg.get('agents',{}).get('defaults',{}).get('models',{})
print('allowed models:', list(adm.keys()))
print('defaultModel:', cfg.get('agents',{}).get('defaults',{}).get('model'))
