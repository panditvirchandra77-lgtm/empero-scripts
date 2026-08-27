import json, shutil, time

PATH = '/home/daytona/.openclaw/openclaw.json'
stamp = time.strftime('%Y%m%d-%H%M%S')
shutil.copy(PATH, PATH + '.bak-empero-' + stamp)

cfg = json.load(open(PATH))
models = cfg.setdefault('models', {})
providers = models.setdefault('providers', {})

providers['empero'] = {
    "baseUrl": "https://free.empero.org/v1",
    "apiKey": "free",
    "api": "openai-completions",
    "models": [
        {"id": "glm-5.3-flash", "name": "GLM 5.3 Flash (Empero)", "api": "openai-completions", "contextWindow": 128000, "maxTokens": 8192},
        {"id": "qwen3.8-flash", "name": "Qwen 3.8 Flash (Empero)", "api": "openai-completions", "contextWindow": 128000, "maxTokens": 8192}
    ]
}

print('providers now:', list(providers.keys()))
json.dump(cfg, open(PATH, 'w'), indent=2)
print('saved OK')
