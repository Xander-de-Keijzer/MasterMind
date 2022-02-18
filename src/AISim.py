from Game import Game
from GameData import GameData, Guess, GameType
from View import ViewType, View
from Solver import AI, AIType


class SimGame:
    def __init__(self, game_: Game, ai_):
        """
        Create a new simulated game for testing
        @param game_: The game to be simulated
        @param ai_: The AI to be used
        """
        self.game = game_
        self.ai = ai_

    def run(self):
        """
        Run a simulated game
        @return: A result message and the amount of guesses it took to reach that result
        """
        c = 0
        while True:
            c += 1
            next_guess, _ = self.ai.new_guess()
            self.game.fill_answer(next_guess)
            self.game.data.guesses.append(next_guess)
            if next_guess == self.game.data.secret:
                return "Victory", c
            if len(self.game.data.guesses) == 11:
                return "Game over", 10


def choose_ai():
    """
    Let the user choose an AI
    @return: The chosen AI as AI_type
    """
    for type_ in AIType:
        print(f"{type_.name} = {type_.value}")
    choice = input("Choose an AI: ")
    for type_ in AIType:
        if str(type_.value) == choice:
            return type_
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
    print(f"{v}/100 won, avg guesses {tn / 1000}")
