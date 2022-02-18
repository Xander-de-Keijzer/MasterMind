from View import *
from GameData import Guess, Color
from Solver import AI, AI_type
from Utils import calc_answer, color_of

class Game:
    def __init__(self) -> None:
        if self.choose_mode():
            self.init_play()
        else:
            self.init_watch()

    def choose_mode(self) -> bool:
        '''
        Let the user choose if they want to play or watch an ai play

        Returns:
            bool: True if play or False if watch
        '''
        inp = input("Play or Watch (P|W): ").lower()
        if inp.startswith("p"):
            return True
        elif inp.startswith("w"):
            return False
        else:
            return self.choose_mode()

    def init_play(self):
        self.data = GameData(GameType.HUMAN_SOLVING)
        self.view = View(ViewType.CLI, self.data)
        PlayGame(self)
        
    def init_watch(self):
        self.data = GameData(GameType.AI_SOLVING)
        self.view = View(ViewType.CLI, self.data)
        WatchGame(self)

    def new_guess(self, opt=""):
        self.view.draw()
        inp = input(f"{opt}: ").lower().replace(" ", "")
        if len(inp) == 4:
            colors = [color_of(self.data.colors, c) for c in inp]
            if Color.NONE not in colors:
                return Guess(colors[0], colors[1], colors[2], colors[3])
        return self.new_guess()  # Recursive call if input is wrong

    def fill_answer(self, guess: Guess):
        guess.black_pegs, guess.white_pegs = calc_answer(guess, self.data.secret)

    

class PlayGame:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.play()

    def play(self):
        while True:
            next_guess = self.game.new_guess()
            self.game.fill_answer(next_guess)
            self.game.data.guesses.append(next_guess)
            if next_guess == self.game.data.secret:
                self.game.view.victory()
                break
            if len(self.game.data.guesses) == 11:
                self.game.view.game_over()
                break
        self.game.__init__()

class WatchGame:
    def __init__(self, game: Game) -> None:
        self.game = game
        self.ai = AI(self.game, self.choose_ai())
        self.choose_secret()
        self.start()

    def choose_ai(self):
        for ai in AI_type:
            print(f"{ai.name} = {ai.value}")
        choice = input("Choose an AI: ")
        for ai in AI_type:
            if str(ai.value) == choice:
                return ai
        return self.choose_ai()

    def choose_secret(self):
        self.game.data.secret = self.game.new_guess("Secret")

    def start(self):
        while True:
            next_guess, n = self.ai.new_guess()
            self.game.fill_answer(next_guess)
            self.game.data.guesses.append(next_guess)
            self.game.view.draw()
            print(f"Posible answers: {n}")
            if next_guess == self.game.data.secret:
                self.game.view.victory()
                break
            if len(self.game.data.guesses) == 11:
                self.game.view.game_over()
                break
        self.game.__init__()
            
if __name__ == "__main__":
    game = Game()

