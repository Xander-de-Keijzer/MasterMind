from enum import Enum, auto
from GameData import Guess
from Utils import calc_all_questions, calc_answer, color_of
from GameData import Color
from time import sleep
from random import choice

def lst_to_question(clrs, lst) -> Guess:
    guess = Guess(
                color_of(clrs, lst[0]), 
                color_of(clrs, lst[1]), 
                color_of(clrs, lst[2]),
                color_of(clrs, lst[3]))
    return guess

class AI_type(Enum):
    RANDOM = auto()
    SHAPIRO = auto()
    YAMS = auto()
    CUSTOM = auto()

class AI:
    def __init__(self, game, type: AI_type) -> None:
        self.game = game
        self.type = type
        self.already_guessed = []

    def filter_question(self, question, answered_question: Guess) -> bool:

        clrs = self.game.data.colors
        q = lst_to_question(clrs, question)
        b, w = calc_answer(q, answered_question)
        if b < answered_question.black_pegs:
            return False
        if w < answered_question.white_pegs:
            return False
        return True

    def filter_questions(self, questions, answered_question: Guess):
        return list(filter(lambda x: self.filter_question(x, answered_question), questions))

    def calc_posible_questions(self):
        colors = [c.name[0] for c in self.game.data.colors if c != Color.NONE]
        all_questions = calc_all_questions(colors, 4)
        for answer in self.game.data.guesses:
            all_questions = self.filter_questions(all_questions, answer)
        return list(filter(lambda x: x not in self.already_guessed, all_questions))

    def new_guess(self):
        sleep(1)
        posible_questions = self.calc_posible_questions()
        if self.type == AI_type.RANDOM:
            rand = choice(posible_questions)
            self.already_guessed.append(rand)
            clrs = self.game.data.colors
            guess = lst_to_question(clrs, rand)
            return guess, len(posible_questions)
        else:
            pass