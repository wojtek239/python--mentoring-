import json

data = {
    'employees': [
        {
            'name': 'Jan Kowalski',
            'specialization': 'Marketing',
            'place': 'Remote'
        },
        {
            'name': 'Jan Nowak',
            'specialization': 'Programming',
            'place': 'Devs-mentoring'
        },
        {
            'name': 'Marcin Nowak',
            'specialiation': 'PO',
            'place': 'Devs-hunting'
        }
    ]
}

with open('json_data.json', 'w') as outfile:
    json.dump(data, outfile)