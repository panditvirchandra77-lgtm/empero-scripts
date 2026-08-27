import json, shutil, sys, time

PATH = '/home/daytona/.openclaw/openclaw.json'
key = sys.argv[1] if len(sys.argv) > 1 else ''
if not key:
    print('ERROR: no api key arg'); sys.exit(1)

stamp = time.strftime('%Y%m%d-%H%M%S')
shutil.copy(PATH, PATH + '.bak-sensenova-' + stamp)

cfg = json.load(open(PATH))
models = cfg.setdefault('models', {})
providers = models.setdefault('providers', {})

providers['sensenova'] = {
    "baseUrl": "https://token.sensenova.ai/v1",
    "apiKey": key,
    "api": "openai-completions",
    "models": [
        {"id": "sensenova-6.8-flash-lite", "name": "SenseNova 6.8 Flash Lite", "api": "openai-completions", "contextWindow": 262144, "maxTokens": 65536},
        {"id": "sensenova-6.7-flash-lite", "name": "SenseNova 6.7 Flash Lite", "api": "openai-completions", "contextWindow": 262144, "maxTokens": 65536}
    ]
}

print('providers now:', list(providers.keys()))
json.dump(cfg, open(PATH, 'w'), indent=2)
print('saved OK')
