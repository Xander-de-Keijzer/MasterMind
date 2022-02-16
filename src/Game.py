from View import *
from GameData import Guess

class Game:
    def __init__(self) -> None:
        if self.init():
            self.init_play()
        else:
            self.init_watch()

    def init_play(self):
        self.data = GameData(GameType.HUMAN_SOLVING)
        self.view = View(ViewType.CLI, self.data)
        PlayGame(self)
        
    def init_watch(self):
        pass

    def init(self) -> bool:
        inp = input("Play or Watch (P|W): ").lower()
        if inp.startswith("p"):
            return True
        elif inp.startswith("w"):
            return False
        else:
            return self.init()

class PlayGame:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.play()

    def play(self):
        next_guess = Guess()
        while True:
            inp = input(":")
            self.game.view.draw()
            print(inp, end="")

if __name__ == "__main__":
    game = Game()

