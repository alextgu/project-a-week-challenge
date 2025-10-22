class Chip:
    """
    A parent class for all chips
    """
    BLACK = 100
    GREEN = 50
    BLUE = 25
    RED = 10
    WHITE = 1
    def __init__(self, colour: str):
        if colour == "BLACK":
            self.value = self.BLACK
        elif colour == "GREEN":
            self.value = self.GREEN
        elif colour == "blue":
            self.value = self.BLUE
        elif colour == "red":
            self.value = self.RED
        elif colour == "white":
            self.value = self.WHITE
