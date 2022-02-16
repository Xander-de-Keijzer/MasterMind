from GameData import GameData, GameType
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
        for i in range(100):
            print("")
        if self.data.game_type == GameType.HUMAN_SOLVING:
            print("[ * * * * ]")
        else:
            print(self.data.secret.cli())
        print("-----------")

v = View(ViewType.CLI, GameData(GameType.HUMAN_SOLVING))
v.draw()
