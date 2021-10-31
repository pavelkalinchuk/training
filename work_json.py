import json

with open('sw_templates.json', 'r') as f:
    data = json.load(f)

print(data)
