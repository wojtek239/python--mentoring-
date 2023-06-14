import json


def reverse_kwargs(**kwargs) -> dict[str, str]:
    reversed_dict = {value: key for key, value in kwargs.items()}

    with open('output.json', 'w') as file:
        json.dump(reversed_dict, file)


def main():
    reverse_kwargs(klucz1='val1', klucz2='val2')


if __name__ == "__main__":
    main()
