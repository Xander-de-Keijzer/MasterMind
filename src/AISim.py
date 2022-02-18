from View import *
from GameData import Guess, Color
from Solver import AI, AI_type
from Utils import calc_answer, color_of
from Game import *

class SimGame:
    def __init__(self, game: Game, ai) -> None:
        self.game = game
        self.ai = ai

    def run(self):
        c = 0
        while True:
            c += 1
            next_guess, n = self.ai.new_guess()
            self.game.fill_answer(next_guess)
            self.game.data.guesses.append(next_guess)
            if next_guess == self.game.data.secret:
                return "Victory", c
                break
            if len(self.game.data.guesses) == 11:
                return "Game over", 10
                break

def choose_ai():
    for ai in AI_type:
        print(f"{ai.name} = {ai.value}")
    choice = input("Choose an AI: ")
    for ai in AI_type:
        if str(ai.value) == choice:
            return ai
    return choose_ai()

if __name__ == "__main__":
    ai_type = choose_ai()
    v = tn = 0
    for i in range(1000):
        data = GameData(GameType.AI_SOLVING)
        view = View(ViewType.CLI, data)
        game = Game(False, data, view)
        game.sim(Guess().randomize())
        ai = AI(game, ai_type)
        sim = SimGame(game, ai)
        r, n = sim.run()
        print(f"Game {i}: {r} in {n} guesses")
        
        if r == "Victory":
            tn += n
            v += 1
        else:
            print(f"guesses = {game.data.guesses} secret = {game.data.secret}")
    print(f"{v}/100 won, avg guesses {tn/1000}")
