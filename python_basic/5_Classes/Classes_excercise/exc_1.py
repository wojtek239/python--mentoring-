class Student:
    def __init__(self, name_: str, age_: int, year_of_study_: int, index_nr_: str):
        self.name = name_
        self.age = age_
        self.year_of_study = year_of_study_
        self.index_nr = index_nr_

    def __str__(self):
        message = (
            f"""
            Name: {self.name}
            Age: {self.age}
            Year of study: {self.year_of_study}
            Index nr: {self.index_nr}
            """
        )
        return message

    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Year of study: {self.year_of_study}')
        print(f'Index nr: {self.index_nr}')


student1 = Student("Krzysiu", "21", 2, "clng2")

student1.show_info()
print(student1)
