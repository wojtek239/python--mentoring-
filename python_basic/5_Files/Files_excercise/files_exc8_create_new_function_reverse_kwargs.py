import json

dictionary = {}


def reverse_kwargs(**kwargs):
    reversed_dict = {value: key for key, value in kwargs.items()}

    with open('output.json', 'w') as file:
        json.dump(reversed_dict, file)


reverse_kwargs(klucz1='val1', klucz2='val2')
