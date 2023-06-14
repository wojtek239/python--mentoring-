import random


class Card:
    def __init__(self, value_: str, suit_: str):
        self.value = value_
        self.suit = suit_

    def __str__(self):
        return f'{self.value} - {self.suit}'


class  Deck:
    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()


for card in Deck.cards:
    print(card)
