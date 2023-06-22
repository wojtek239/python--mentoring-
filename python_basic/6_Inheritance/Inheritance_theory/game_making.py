class Character:
    def __init__(self, name, start_items, abilities_):
        self.player_name = name
        self.hp = 100
        self.gold = 50
        self.inventory = start_items
        self.abilities = abilities_

    def add_to_inventory(self, new_item):
        self.inventory.append(new_item)

    def use_ability(self, name):
        if name in self.abilities:
            print(self.abilities.get(name))
        else:
            print("unknown ability")

    def tell(self):
        print("howdy, i'm ", self.player_name)


class Blacksmith(Character):
    def __init__(self, name):
        super().__init__(name, ['hammer'], {'improving items': 'an item has been '
                                                               'improved'})

    def tell(self):
        super().tell()
        print("i can repair ur stuff...")


class Elf(Character):
    def __init__(self, name):
        super().__init__(name, ['bow', 'knife'], {'shooting': 'just shot a bow...',
                                                  'attack': 'just attacked with '
                                                            'knife...'})

    def tell(self):
        super().tell()
        print('fight or die')


if __name__ == "__main__":
    elf = Elf("Legolas")
    blacksmith = Blacksmith("Jack")

    elf.tell()
    elf.add_to_inventory("item1")
    elf.use_ability("shooting")

    print()

    blacksmith.tell()
    blacksmith.use_ability("attack")

