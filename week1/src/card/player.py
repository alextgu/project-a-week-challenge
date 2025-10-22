from card.card import Card
from game.chips import Chip

class Player:
    """
    A player object has a name, a hand, and a total amount of chips
    """
    name: str
    hand: list[Card]
    chips: list[Chip]
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.chips = []

    def add_chip(self, chip: Chip):
        self.chips.append(chip)

    def remove_chip(self, chip: Chip):
        self.chips.remove(chip)
    
    def hit(self):
        pass

    def show_hand(self):
        pass