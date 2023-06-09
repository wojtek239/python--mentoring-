class Human:
    """  opis klasy """
    def __init__(self, name_: str, gender_: str, age_: int):
        self.name = name_
        self.gender = gender_
        self.age = age_


def main():
    person1 = Human("kacper", "m", 42)
    person2 = Human("kinga", "w", 120)

    print(f"first person name is: ", person1.name)
    print(f"second person name is: ", person2.name)


if __name__ == "__main__":
    main()
