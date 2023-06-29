class Notes:
    def __init__(self):
        self.notes = []

    def add(self):
        """
        to add new note
        """
        note = input("Pls add new note: ")
        self.notes.append(note)
        print("Note added.")

    def show(self):
        """
        to show existing notes
        """
        if not self.notes:
            print("There is no such note.")
        else:
            print("Notes list:")
            for note in self.notes:
                print(note)


class Cards:
    def __init__(self):
        self.cards = []

    def add(self):
        """
        to add new card
        """
        card = input("Pls add new card: ")
        self.cards.append(card)
        print("Card added.")

    def show(self):
        """
        to show existing cards
        """
        if not self.cards:
            print("There is no such card.")
        else:
            print("Cards list:")
            for card in self.cards:
                print(card)


class Manager:
    def __init__(self):
        self.menu_options = {
            "1": "Add note",
            "2": "Add card",
            "3": "Show all notes",
            "4": "Show all cards",
            "5": "Exit"
        }
        self.notes = Notes()
        self.cards = Cards()

    def start(self):
        """
        to start program
        """
        while True:
            self.show_menu()
            choice = self.get_choice()

            if choice == "1":
                self.notes.add()

            elif choice == "2":
                self.cards.add()

            elif choice == "3":
                self.notes.show()

            elif choice == "4":
                self.cards.show()

            elif choice == "5":
                print("Exit program.")
                break

            else:
                print("Wrong choice.")

    def show_menu(self):
        """
        to show menu
        """
        print("Menu:")
        for number, option in self.menu_options.items():
            print(f"{number}. {option}")

    def get_choice(self):
        """
        to choose an option from menu
        """
        choice = input("Choose option: ")
        return choice


manager = Manager()
manager.start()
