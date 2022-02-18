from GameData import GameData, GameType, Color, Guess
from View import View, ViewType
from Utils import color_of, calc_answer
from Solver import AI, AIType


class Game:
    def __init__(self, run=True, data=None, view=None):
        """
        Create a new Game object
        @param run: If the game should start running
        @param data: optional GameData to be pre-defined for simulation
        @param view: optional View to be pre-defined for simulation
        """
        if not run:
            self.data = data
            self.view = view
        else:
            if self.choose_mode():
                self.init_play()
            else:
                self.init_watch()

    def sim(self, secret):
        """
        Define the secret for simulations
        @param secret:
        """
        self.data.secret = secret

    def choose_mode(self) -> bool:
        """
        Let the user choose if they want to play or watch an ai play
        @return: True if play or False if watch
        """
        inp = input("Play or Watch (P|W): ").lower()
        if inp.startswith("p"):
            return True
        elif inp.startswith("w"):
            return False
        else:
            return self.choose_mode()

    def init_play(self):
        """
        Initialize a game where the user can guess
        """
        self.data = GameData(GameType.HUMAN_SOLVING)
        self.view = View(ViewType.CLI, self.data)
        PlayGame(self)

    def init_watch(self):
        """
        Initialize a game where an AI is guessing
        """
        self.data = GameData(GameType.AI_SOLVING)
        self.view = View(ViewType.CLI, self.data)
        WatchGame(self)

    def new_guess(self, opt=""):
        """
        Request a new guess from the user
        @param opt: An optional message to explain the type of guess
        """
        self.view.draw()
        inp = input(f"{opt}: ").lower().replace(" ", "")
        if len(inp) == 4:
            colors = [color_of(self.data.colors, c) for c in inp]
            if Color.NONE not in colors:
                return Guess(colors[0], colors[1], colors[2], colors[3])
        return self.new_guess()  # Recursive call if input is wrong

    def fill_answer(self, guess: Guess):
        """
        Fill the answer of a guess
        @param guess: The guess to receive an answer
        """
        guess.black_pegs, guess.white_pegs = calc_answer(guess, self.data.secret)


class PlayGame:
    def __init__(self, game_: Game):
        """
        Create a new PlayGame class
        @param game_: The game holding the game data
        """
        self.game = game_
        self.play()

    def play(self):
        """
        Start the game
        """
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
    def __init__(self, game_: Game):
        """
        Create a new WatchGame class
        @param game_: The game holding the game data
        """
        self.game = game_
        self.ai = AI(self.game, self.choose_ai())
        self.choose_secret()
        self.start()

    def choose_ai(self):
        """
        Let the user choose an AI
        @return: The chosen AI as AI_type
        """
        for ai in AIType:
            print(f"{ai.name} = {ai.value}")
        choice = input("Choose an AI: ")
        for ai in AIType:
            if str(ai.value) == choice:
                return ai
        return self.choose_ai()

    def choose_secret(self):
        """
        Let the user choose a secret code
        """
        self.game.data.secret = self.game.new_guess("Secret")

    def start(self):
        """
        Start the game
        """
        while True:
            next_guess, n = self.ai.new_guess(1)
            self.game.fill_answer(next_guess)
            self.game.data.guesses.append(next_guess)
            self.game.view.draw()
            print(f"Possible answers: {n}")
            if next_guess == self.game.data.secret:
                self.game.view.victory()
                break
            if len(self.game.data.guesses) == 11:
                self.game.view.game_over()
                break
        self.game.__init__()


if __name__ == "__main__":
    game = Game()
