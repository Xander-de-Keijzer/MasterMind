from View import *
from GameData import Guess, Color, Answer
from Solver import AI, AI_type

def ask_question(question: Guess, solution: Guess):
    q = question.lst()
    s = solution.lst()
    r = []
    b = w = 0
    for i in range(len(q)):
        if q[i] == s[i]:
            b += 1
            r.append(i)
    for d in reversed(r):
        del q[d]
        del s[d]
    for i in range(len(q)):
        for j in range(len(s)):
            if q[i] == s[j]:
                w += 1
                del s[j]
                break
    return b, w

class Game:
    def __init__(self) -> None:
        
        if self.init():
            self.init_play()
        else:
            self.init_watch()

    def new_guess(self, draw=True):
        if draw:
            self.view.draw()
        inp = input(": ").lower().replace(" ", "")
        if len(inp) == 4:
            colors = []
            for c in inp:
                color = self.color_of(c)
                if color == Color.NONE:
                    break
                colors.append(color)
            if len(colors) == 4:
                return Guess(colors[0], colors[1], colors[2], colors[3])
        return self.new_guess()

    def fill_answer(self, guess: Guess):
        black, white = ask_question(guess, self.data.secret)
        for _ in range(black):
            guess.answer.append(Answer.BLACK)
        for _ in range(white):
            guess.answer.append(Answer.WHITE)

    def color_of(self, char):
        for color in self.data.colors:
            if color.name.lower().startswith(char.lower()):
                return color
        return Color.NONE

    def init_play(self):
        self.data = GameData(GameType.HUMAN_SOLVING)
        self.view = View(ViewType.CLI, self.data)
        PlayGame(self)
        
    def init_watch(self):
        self.data = GameData(GameType.AI_SOLVING)
        self.view = View(ViewType.CLI, self.data)
        WatchGame(self)

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
        self.ai = AI(self, AI_type.RANDOM)
        self.choose_secret()
        self.start()

    def choose_secret(self):
        self.game.data.secret = self.game.new_guess(False)

    def start(self):
        while True:
            next_guess = self.ai.new_guess()
            self.game.fill_answer(next_guess)
            self.game.data.guesses.append(next_guess)
            self.game.view.draw()
            if next_guess == self.game.data.secret:
                self.game.view.victory()
                break
            if len(self.game.data.guesses) == 11:
                self.game.view.game_over()
                break
        self.game.__init__()
            
if __name__ == "__main__":
    game = Game()

