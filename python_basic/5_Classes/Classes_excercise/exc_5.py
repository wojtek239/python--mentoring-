import random
from typing import Optional


class Card:
    def __init__(self, value_: str, suit_: str):
        self.value = value_
        self.suit = suit_

    def __str__(self):
        return f'{self.value} - {self.suit}'


class Deck:
    SUITS = ["Diamonds", "Clubs", "Hearts", "Spades"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = []
        self.create_deck()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Optional[Card]:
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()

    def create_deck(self):
        self.cards.clear()

        for suit in self.SUITS:
            for value in self.VALUES:
                card = Card(value, suit)
                self.cards.append(card)


def main():
    deck = Deck()
    for card in deck.cards:
        print(card)


if __name__ == "__main__":
    main()
