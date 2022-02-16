from View import *
from GameData import Guess, Color, Answer

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

    def fill_answer(self, guess: Guess):
        black, white = ask_question(guess, self.data.secret)
        for _ in range(black):
            guess.answer.append(Answer.BLACK)
        for _ in range(white):
            guess.answer.append(Answer.WHITE)

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
        self.game.data.guesses.append(next_guess)
        while True:
            self.game.view.draw()
            inp = input(":")
            color = self.color_of(inp)
            if color != Color.NONE and next_guess.add(color):
                self.game.fill_answer(next_guess)
                next_guess = Guess()
                self.game.data.guesses.append(next_guess)
                if len(self.game.data.guesses) == 11:
                    self.game.view.game_over()
                    break
        self.game.__init__()

    def color_of(self, char):
        for color in self.game.data.colors:
            if color.name.lower().startswith(char.lower()):
                return color
        return Color.NONE
            
if __name__ == "__main__":
    game = Game()

