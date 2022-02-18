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
    # Choose a random question from a filtered list of posible questions 
    # based on previous answers, based of https://www.philos.rug.nl/~barteld/master.pdf
    # Simulated results, win-rate=91.2% with avg guesses when won: 6.272
    SHAPIRO = auto()
    # based of https://www.philos.rug.nl/~barteld/master.pdf
    # Simulated results, win-rate=85.7% with avg guesses when won: 6.128
    YAMS = auto()
    # Choose the best question (yielding heighest avg information) from a
    # filtered list of posible questions based on previous answers
    # Simulated results, win-rate=90.0% with avg guesses when won: 6.673
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

    def calc_best_question_custom(self, questions):
        clrs = self.game.data.colors
        best_val = 0
        best_q = questions[0]
        for q1 in questions:
            tb = tw = 0
            for q2 in questions:
                if q1 == q2:
                    continue
                q01 = lst_to_question(clrs, q1)
                q02 = lst_to_question(clrs, q2)
                b, w = calc_answer(q01, q02)
                tb += b * 2
                tw += w
            value = tb + tw
            if value > best_val:
                best_val = value
                best_q = q1
        return best_q

    def calc_best_question_yams(self, questions):
        clrs = self.game.data.colors
        best_val = 0
        best_q = questions[0]
        for q1 in questions:
            lst = []
            for q2 in questions:
                if q1 == q2:
                    continue
                q01 = lst_to_question(clrs, q1)
                q02 = lst_to_question(clrs, q2)
                r = calc_answer(q01, q02)
                if r not in lst:
                    lst.append(r)
            if len(lst) > best_val:
                best_val = len(lst)
                best_q = q1
        return best_q

    def new_guess(self, wait=0):
        sleep(wait)
        posible_questions = self.calc_posible_questions()

        # SHAPIRO
        if self.type == AI_type.SHAPIRO:
            rand = choice(posible_questions)
            self.already_guessed.append(rand)
            clrs = self.game.data.colors
            guess = lst_to_question(clrs, rand)
            return guess, len(posible_questions)

        # YAMS
        if self.type == AI_type.YAMS:
            if len(posible_questions) < 100:
                q = self.calc_best_question_yams(posible_questions)
            else:
                q = choice(posible_questions)
            self.already_guessed.append(q)
            clrs = self.game.data.colors
            guess = lst_to_question(clrs, q)
            return guess, len(posible_questions)

        # CUSTOM
        if self.type == AI_type.CUSTOM:
            if len(posible_questions) < 100:
                q = self.calc_best_question_custom(posible_questions)
            else:
                q = choice(posible_questions)
            self.already_guessed.append(q)
            clrs = self.game.data.colors
            guess = lst_to_question(clrs, q)
            return guess, len(posible_questions)