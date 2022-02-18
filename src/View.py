from GameData import GameData, GameType, Color
from enum import Enum, auto

class ViewType(Enum):
    GUI = auto()
    CLI = auto()

class View:
    def __init__(self, type: ViewType, data: GameData) -> None:
        self.type = type
        self.data = data

    def draw(self, clear=True):
        if self.type == ViewType.GUI:
            pass
        else:
            self.draw_cli(clear)

    def draw_cli(self, clear=True):
        if clear:
            self.clear_screen()
        print("Colors: ", end="")
        for color in self.data.colors:
            if color != Color.NONE:
                print(color.name[0], end="")
        print("")
        if self.data.game_type == GameType.HUMAN_SOLVING:
            print("  [ * * * * ]")
            #print(self.data.secret.cli())
        else:
            print(self.data.secret.cli())
        print("----------------------")
        for ind, guess in enumerate(self.data.guesses):
            print(f"{ind+1}: {guess.cli()}")

    def victory(self):
        self.draw()
        print("\nYou guessed the code!")
        print(f"Secret: {self.data.secret.cli()}")

    def game_over(self):
        self.draw()
        print("\nGame over")
        print(f"Secret: {self.data.secret.cli()}")

    def clear_screen(self, rng=100):
        for i in range(rng):
            print("")
