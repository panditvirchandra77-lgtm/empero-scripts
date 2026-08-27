import json, shutil, time
PATH = '/home/daytona/.openclaw/openclaw.json'
stamp = time.strftime('%Y%m%d-%H%M%S')
shutil.copy(PATH, PATH + '.bak-addmodel-' + stamp)
cfg = json.load(open(PATH))
adm = cfg.setdefault('agents',{}).setdefault('defaults',{}).setdefault('models',{})
adm['openrouter/deepseek/deepseek-v4-flash'] = {}
print('allowed now:', list(adm.keys()))
json.dump(cfg, open(PATH,'w'), indent=2)
print('saved OK')
