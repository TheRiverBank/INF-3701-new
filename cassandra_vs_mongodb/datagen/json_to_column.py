import json

with open("data.json", 'r') as f:
    data = json.loads(f.readlines()[0])


column_names = []

for key, val in data:
    for 