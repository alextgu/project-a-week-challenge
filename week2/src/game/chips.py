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
        elif colour == "BLUE":
            self.value = self.BLUE
        elif colour == "RED":
            self.value = self.RED
        elif colour == "WHITE":
            self.value = self.WHITE
