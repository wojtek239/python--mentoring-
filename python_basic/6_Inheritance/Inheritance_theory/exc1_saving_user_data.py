class User:
    def __init__(self, name_, email_, password_):
        self.name = name_
        self.email = email_
        self.password = password_

    def __str__(self):
        return self.name + " " + self.email + " " + self.password

class Program:
    def __init__(self):
        self.if_open = Trur
        self.users = []

    def add_user(self):
        name = input("pls enter name:")
        email = input("pls enter email:")
        password = input("pls enter password:")

        new_user = User(name, email, password)
        self.users.append(new_user)

    def save(self):
        with open("users.txt", "a") as file:
            for user in self.users:
                file.writeln(str(user))

    def show_menu(self):
        while(self.if_open):
            """
            choose action:
            1 - add user
            2 - save to file
            3 - end program
            """
            choice = input()
            self.do_from_menu(choice)

    def do_from_menu(self, choice):
        if choice == '1':
            self.add_user()
        elif choice == '2':
            self.save()
        elif choice == '3':
            self.if_open = False
        else:
            print("unknown command")

def main():
    menu = Program()

    manu.show_menu()


if __name__ == "__main__":
    main()