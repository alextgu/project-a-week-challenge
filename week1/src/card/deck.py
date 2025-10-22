from card.card import Card
import random

class Deck:
    """
    A deck object has 52 cards, 13 ranks for each of the 4 suits
    """
    cards = list[Card]

    def __init__(self):
        cards = []

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, num_cards: int) -> list[cards]:
        """
        Deals a number of cards from the top of the deck
        """
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck")
        self.cards.pop(num_cards)
        return self.cards[-num_cards:]
    
    def reset(self):
        """
        Resets the deck to a new deck of 52 cards
        """
        self.cards = []
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.cards.append(Card(suit, rank))
        self.shuffle()

