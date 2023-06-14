import json

intro = (
    """
    Interface Status
    ================================================================================
    DN                                                 Description           Speed    
    MTU  
    """
)
with open('data.json') as file:
    data = json.load(file)

for row in data['imdata']:
    dn = row['l1PhysIf']['attributes']['dn']
    description = row['l1PhysIf']['attributes']['descr']
    speed = row['l1PhysIf']['attributes']['speed']
    mtu = row['l1PhysIf']['attributes']['mtu']
    
    print(intro)
    print("{:<7}{:>11}{:>25}\n{}\n".format(dn, description, speed, mtu))