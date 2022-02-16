from enum import Enum, auto
from GameData import Guess

class AI_type(Enum):
    RANDOM = auto()
    SHAPIRO = auto()
    YAMS = auto()
    CUSTOM = auto()

class AI:
    def __init__(self, game, type: AI_type) -> None:
        self.game = game
        self.type = type

    def new_guess(self):
        if self.type == AI_type.RANDOM:
            return Guess().randomize()
        else:
            pass