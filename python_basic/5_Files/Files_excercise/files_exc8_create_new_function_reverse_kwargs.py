import json

with open('data.json') as file:
    data = json.load(file)

for package in data['packages']:
    dn = package['DN']
    description = package['Description']
    speed = package['Speed']
    mtu = package['MTU']


print(f'{dn}, {description}, {speed}, {mtu}')