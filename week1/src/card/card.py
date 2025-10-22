class Card:
    """
    A Card object of a standard deck of cards (Does not include jokers)
    """
    suit: str 
    rank: str

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
