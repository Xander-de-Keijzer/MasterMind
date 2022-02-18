import random
from GameData import Color


def color_of(colors, char):
    """
    Get a color from a character
    @param colors: The list of colors to search from
    @param char: The character to search
    @return: The found Color else Color.NONE
    """
    for color in colors:
        if color.name.lower().startswith(char.lower()):
            return color
    return Color.NONE


def calc_all_questions(colors, positions):
    """
    Calculate all possible answers of a game
    @param colors: The possible colors of the game
    @param positions: The amount of positions to place colors
    @return: The list of possible solutions of this game
    """
    if positions <= 1:
        return colors
    lower_list = calc_all_questions(colors, positions - 1)
    new_list = []
    for lower in lower_list:
        for color in colors:
            new_list.append(f"{color}{lower}")
    return new_list


def calc_answer(question, solution):
    """
    Calculate the black and white pegs of a question
    @param question: The question that is asked
    @param solution: The secret solution
    @return: black, white pegs
    """
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


####################################################
# Example implementations
####################################################

Colors = []
Positions = 0


def random_question():
    questions = calc_all_questions(Colors, Positions)
    solution = random.choice(questions)
    question = random.choice(questions)
    answer = calc_answer(question, solution)
    print(f"{question}: {answer} -- {solution}")


def question_values():
    questions = calc_all_questions(Colors, Positions)
    for q in questions:
        value = calc_answer(q, questions)
        print(f"{q=} {value=}")
