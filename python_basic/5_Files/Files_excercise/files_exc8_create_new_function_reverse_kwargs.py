import json


def reverse_dict(**kwargs: dict) -> dict[str, str]:
    new_dict = {}

    for k, v in kwargs.items():
        new_dict[v] = k

    return new_dict


def main():
    songs = {
        'The Sensual World': 'Kate Bush',
        'Shaday': 'Ofra Haza',
        'Achtung Baby': 'U2',
        'Aion': 'Dead Can Dance',
        'Invisible Touch': 'Genesis'
    }
    data = reverse_dict(**songs)
    with open("output.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
