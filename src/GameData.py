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
    ORANGE = auto()
    NONE = 99

    def char(self):
        """
        Get the first character of the Color name
        @return: The first character or * of NONE
        """
        if self == Color.NONE:
            return "*"
        else:
            return self.name[0]

    def __repr__(self) -> str:
        return self.name.lower()

    def __str__(self) -> str:
        return self.__repr__()


def random():
    """
    Get a random color
    @return: A new random Color enum
    """
    return Color(randint(1, 6))


class Guess:
    def __init__(self, c1: Color = Color.NONE, c2: Color = Color.NONE, c3: Color = Color.NONE, c4: Color = Color.NONE):
        """
        A class to hold the data of a Guess
        @param c1: The first color of the Guess
        @param c2: The second color of the Guess
        @param c3: The third color of the Guess
        @param c4: The fourth color of the Guess
        """
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.black_pegs = 0
        self.white_pegs = 0

    def randomize(self):
        """
        Randomize the colors of this guess
        @return: The instance of this class for chaining
        """
        self.c1 = random()
        self.c2 = random()
        self.c3 = random()
        self.c4 = random()
        return self

    def lst(self):
        """
        Create a list of the colors in this guess with only the first char of each color
        @return: A list of each char
        """
        return [self.c1.char(), self.c2.char(), self.c3.char(), self.c4.char()]

    def cli(self):
        """
        Format a guess for CLI
        @return: The formatted string with class data
        """
        a = self.cli_answer()
        if len(a) == 0:
            return f"[ {self.c1.char()} {self.c2.char()} {self.c3.char()} {self.c4.char()} ]"
        else:
            return f"[ {self.c1.char()} {self.c2.char()} {self.c3.char()} {self.c4.char()} ] ({self.cli_answer()})"

    def cli_answer(self):
        """
        Format the black and white pegs for CLI
        @return: The formatted string
        """
        b = "".join("B" for _ in range(self.black_pegs))
        w = "".join("W" for _ in range(self.white_pegs))
        return f"{b}{w}"

    def __eq__(self, other):
        return self.c1 == other.c1 and self.c2 == other.c2 and self.c3 == other.c3 and self.c4 == other.c4

    def __repr__(self) -> str:
        return f"({self.c1}, {self.c2}, {self.c3}, {self.c4})"

    def __str__(self) -> str:
        return self.__repr__()


class GameData:
    def __init__(self, game_type: GameType):
        """
        Create a new GameData object
        @param game_type: The game type of this data
        """
        self.game_type = game_type
        self.colors = [Color.RED, Color.GREEN, Color.WHITE, Color.BLACK, Color.YELLOW, Color.ORANGE]
        self.secret = Guess()
        self.guesses: list[Guess] = []
        if game_type == GameType.HUMAN_SOLVING:
            self.secret.randomize()

    def __repr__(self) -> str:
        return f"({self.game_type=}, {self.colors=}, {self.secret=}, {self.guesses=})"

    def __str__(self) -> str:
        return self.__repr__()
