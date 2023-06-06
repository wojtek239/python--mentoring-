class Human:
    def __init__(self, name_, gender_, age_):
        self.name = name_
        self.gender = gender_
        self.age = age_

def main():
    person1 = Human("kacper", "m", 42)
    person2 = Human("kinga", "w", 120)

    print(f"first person name is: ", person1.name)

if __name__ == "__main__":
    main()
