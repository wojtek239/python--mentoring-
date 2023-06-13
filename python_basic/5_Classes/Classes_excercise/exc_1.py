class Student:
    def __init__(self, name_, age_, year_of_study_, index_nr_):
        self.name = name_
        self.age = age_
        self.year_of_study = year_of_study_
        self.index_nr = index_nr_

    def show_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Year of study: {self.year_of_study}')
        print(f'Index nr: {self.index_nr}')


student1 = Student("Krzysiu", "21", 2, "clng2")

student1.show_info()