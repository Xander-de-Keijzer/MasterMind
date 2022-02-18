from GameData import GameData, GameType, Color
from enum import Enum, auto


class ViewType(Enum):
    """
    Create a ViewType enum for defining the type of View
    """
    GUI = auto()
    CLI = auto()


def clear_screen(rng=100):
    """
    Print empty lines to clear the CLI screen
    @param rng: The amount of empty lines to print
    """
    for i in range(rng):
        print("")


class View:
    def __init__(self, type_: ViewType, data: GameData):
        """
        Create a new View class, used for handling the output to the user
        @param type_: The type of View to be generated
        @param data: The data from which the view is generated
        """
        self.type = type_
        self.data = data

    def draw(self, clear=True):
        """
        Draw the new data to the screen
        @param clear: If the screen should be cleared
        """
        if self.type == ViewType.GUI:
            pass
        else:
            self.draw_cli(clear)

    def draw_cli(self, clear=True):
        """
        Draw the new data to the screen using the CLI
        @param clear: If the screen should be cleared
        """
        if clear:
            clear_screen()
        print("Colors: ", end="")
        for color in self.data.colors:
            if color != Color.NONE:
                print(color.name[0], end="")
        print("")
        if self.data.game_type == GameType.HUMAN_SOLVING:
            print("  [ * * * * ]")
        else:
            print(self.data.secret.cli())
        print("----------------------")
        for ind, guess in enumerate(self.data.guesses):
            print(f"{ind + 1}: {guess.cli()}")

    def victory(self):
        """
        Called when the game is won to display a victory message
        """
        self.draw()
        print("\nYou guessed the code!")
        print(f"Secret: {self.data.secret.cli()}")

    def game_over(self):
        """
        Called when the game is lost to display a game over message
        """
        self.draw()
        print("\nGame over")
        print(f"Secret: {self.data.secret.cli()}")
