import json, shutil, time, sys
PATH = '/home/daytona/.openclaw/openclaw.json'
stamp = time.strftime('%Y%m%d-%H%M%S')
shutil.copy(PATH, PATH + '.bak-or-rotate-' + stamp)
cfg = json.load(open(PATH))
cfg['models']['providers']['openrouter']['apiKey'] = sys.argv[1]
json.dump(cfg, open(PATH,'w'), indent=2)
print('key rotated OK')
