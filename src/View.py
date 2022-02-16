from GameData import GameData, GameType, Color
from enum import Enum, auto

class ViewType(Enum):
    GUI = auto()
    CLI = auto()

class View:
    def __init__(self, type: ViewType, data: GameData) -> None:
        self.type = type
        self.data = data

    def draw(self):
        if self.type == ViewType.GUI:
            pass
        else:
            self.draw_cli()

    def draw_cli(self):
        self.clear_screen()
        print("Colors: ", end="")
        for color in self.data.colors:
            if color != Color.NONE:
                print(color.name[0], end="")
        print("")
        if self.data.game_type == GameType.HUMAN_SOLVING:
            print(self.data.secret.cli())
        else:
            print(self.data.secret.cli())
        print("-----------")
        for guess in self.data.guesses:
            print(guess.cli())

    def game_over(self):
        self.clear_screen()
        print("Game over")
        print(f"Secret: {self.data.secret.cli()}")

    def clear_screen(self):
        for i in range(100):
            print("")
