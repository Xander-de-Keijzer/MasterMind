from enum import Enum, auto
from random import randint

class GameType(Enum):
    HUMAN_SOLVING = auto()
    AI_SOLVING = auto()

    def __repr__(self) -> str:
        return self.name.lower()

    def __str__(self) -> str:
        return self.__repr__()

class Color(Enum):
    RED = auto()
    GREEN = auto()
    WHITE = auto()
    BLACK = auto()
    YELLOW = auto()
    BLUE = auto()
    NONE = 99

    def random(self):
        return Color(randint(1, 6))

    def char(self):
        if self == Color.NONE:
            return "*"
        else:
            return self.name[0]

    def __repr__(self) -> str:
        return self.name.lower()

    def __str__(self) -> str:
        return self.__repr__()

class Answer(Enum):
    WHITE = auto()
    BLACK = auto()

    def char(self):
        return self.name[0]

class Guess:
    def __init__(self, c1:Color=Color.NONE, c2:Color=Color.NONE, c3:Color=Color.NONE, c4:Color=Color.NONE) -> None:
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.answer: list[Answer] = []

    def randomize(self):
        self.c1 = Color(1).random()
        self.c2 = Color(1).random()
        self.c3 = Color(1).random()
        self.c4 = Color(1).random()
        return self

    def cli(self):
        a = self.cli_answer()
        if len(a) == 0:
            return f"[ {self.c1.char()} {self.c2.char()} {self.c3.char()} {self.c4.char()} ]"
        else:
            return f"({self.cli_answer()}) [ {self.c1.char()} {self.c2.char()} {self.c3.char()} {self.c4.char()} ]"

    def cli_answer(self):
        r = ""
        for a in self.answer:
            r = f"{r}{a.char()}"
        return r

    def __repr__(self) -> str:
        return f"({self.c1}, {self.c2}, {self.c3}, {self.c4})"

    def __str__(self) -> str:
        return self.__repr__()

class GameData:
    def __init__(self, game_type: GameType) -> None:
        self.game_type = game_type
        self.colors = [Color.RED, Color.GREEN, Color.WHITE, Color.BLACK, Color.YELLOW, Color.BLUE]
        self.secret = Guess()
        self.guesses: list[Guess] = []
        if game_type == GameType.HUMAN_SOLVING:
            self.secret.randomize()

    def __repr__(self) -> str:
        return f"({self.game_type=}, {self.colors=}, {self.secret=}, {self.guesses=})"

    def __str__(self) -> str:
        return self.__repr__()
        

if __name__ == "__main__":
    game = GameData(GameType.HUMAN_SOLVING)
    game2 = GameData(GameType.AI_SOLVING)

    print(game)
    print(game2)
