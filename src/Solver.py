from enum import Enum, auto
from GameData import Guess
from Utils import calc_all_questions, calc_answer, color_of
from GameData import Color
from time import sleep
from random import choice


def lst_to_question(clrs, lst) -> Guess:
    """
    Convert a list of characters to a Guess object
    @param clrs: The colors of this game
    @param lst: The list of characters
    @return: The new Guess object
    """
    guess = Guess(
        color_of(clrs, lst[0]),
        color_of(clrs, lst[1]),
        color_of(clrs, lst[2]),
        color_of(clrs, lst[3]))
    return guess


class AIType(Enum):
    # Choose a random question from a filtered list of possible questions
    # based on previous answers, based of https://www.philos.rug.nl/~barteld/master.pdf
    # Simulated results, win-rate=91.2% with avg guesses when won: 6.272
    SHAPIRO = auto()
    # based of https://www.philos.rug.nl/~barteld/master.pdf
    # Simulated results, win-rate=85.7% with avg guesses when won: 6.128
    YAMS = auto()
    # Choose the best question (yielding highest avg information) from a
    # filtered list of possible questions based on previous answers
    # Simulated results, win-rate=90.0% with avg guesses when won: 6.673
    CUSTOM = auto()


class AI:
    def __init__(self, game, type_: AIType):
        """
        Create a new AI object
        @param game: The game holding the game data
        @param type_: The type of AI to be used
        """
        self.game = game
        self.type = type_
        self.already_guessed = []

    def filter_question(self, question, answered_question: Guess) -> bool:
        """
        Check if a question could be used
        @param question: The question to be filtered
        @param answered_question: The answer to be used for filtering
        @return: If the question can be used
        """
        clrs = self.game.data.colors
        q = lst_to_question(clrs, question)
        b, w = calc_answer(q, answered_question)
        if b < answered_question.black_pegs:
            return False
        if w < answered_question.white_pegs:
            return False
        return True

    def filter_questions(self, questions, answered_question: Guess):
        """
        Filter a list of question against an question that has been answered
        @param questions: The questions to be filtered
        @param answered_question: The answer to be used for filtering
        @return: The filtered list
        """
        return list(filter(lambda x: self.filter_question(x, answered_question), questions))

    def calc_possible_questions(self):
        """
        Calculate the possible solutions from a set of answered questions
        @return: A list of possible questions to ask
        """
        colors = [c.name[0] for c in self.game.data.colors if c != Color.NONE]
        all_questions = calc_all_questions(colors, 4)
        for answer in self.game.data.guesses:
            all_questions = self.filter_questions(all_questions, answer)
        return list(filter(lambda x: x not in self.already_guessed, all_questions))

    def calc_best_question_custom(self, questions):
        """
        Find the best question using the Custom AI
        @param questions: The list of questions
        @return: The 'best' question
        """
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
        """
        Find the best question using the Yams AI
        @param questions: The list of questions
        @return: The 'best' question
        """
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
        """
        Request a new guess from the AI
        @param wait: Optional delay
        @return: The new guess
        """
        sleep(wait)
        possible_questions = self.calc_possible_questions()

        # SHAPIRO
        if self.type == AIType.SHAPIRO:
            rand = choice(possible_questions)
            self.already_guessed.append(rand)
            clrs = self.game.data.colors
            guess = lst_to_question(clrs, rand)
            return guess, len(possible_questions)

        # YAMS
        if self.type == AIType.YAMS:
            if len(possible_questions) < 100:
                q = self.calc_best_question_yams(possible_questions)
            else:
                q = choice(possible_questions)
            self.already_guessed.append(q)
            clrs = self.game.data.colors
            guess = lst_to_question(clrs, q)
            return guess, len(possible_questions)

        # CUSTOM
        if self.type == AIType.CUSTOM:
            if len(possible_questions) < 100:
                q = self.calc_best_question_custom(possible_questions)
            else:
                q = choice(possible_questions)
            self.already_guessed.append(q)
            clrs = self.game.data.colors
            guess = lst_to_question(clrs, q)
            return guess, len(possible_questions)
