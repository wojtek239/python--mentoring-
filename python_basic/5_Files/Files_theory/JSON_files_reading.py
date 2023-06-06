import json

with open('json data.json') as json_file:
    data = json.load(json_file)
    print(data)