class Menu:
    @staticmethod
    def show():
        menu = """
        1. Add Note
        2. Add Card
        3. Show all Notes
        4. Show all Cards
        5. Exit
        """
        print(menu)

    @staticmethod
    def get_choice() -> int:
        return int(input("Choose what you want do:"))


class Notes:
    def __init__(self):
        self.notes = []

    def add_note(self):
        """
        to add new note
        """
        note = input("Pls add new note: ")
        self.notes.append(note)
        print("Note added.")

    def show_notes(self):
        """
        to show existing notes # pisac pelnymi zdaniami
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

    def add_card(self):
        """
        to add new card
        """
        card = input("Pls add new card: ")
        self.cards.append(card)
        print("Card added.")

    def show_cards(self):
        """
        to show existing cards
        """
        if not self.cards:
            print("There is no such card.")
        else:
            print("Cards list:")
            for card in self.cards:
                print(card)


class Manager(Cards, Notes):
    def __init__(self):
        Cards.__init__(self)
        Notes.__init__(self)

        self.menu_options = {
            1: self.add_note,
            2: self.add_card,
            3: self.show_notes,
            4: self.show_cards,
            5: quit,
        }

    def start(self):
        """
        to start program
        """
        while True:
            Menu.show()
            user_choice = Menu.get_choice()

            self.menu_options.get(user_choice, self.show_error)()

    def show_error(self):
        print("Wrong choice.")

    # def show_menu(self):
    #     """
    #     to show menu
    #     """
    #     print("Menu:")
    #     for number, option in self.menu_options.items():
    #         print(f"{number}. {option}")
    #
    # def get_choice(self):
    #     """
    #     to choose an option from menu
    #     """
    #     choice = input("Choose option: ")
    #     return choice


def main():
    manager = Manager()
    manager.start()


if __name__ == "__main__":
    main()
# funkcja statyczna
