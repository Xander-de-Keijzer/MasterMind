import random
from GameData import Color

def color_of(colors, char):
    for color in colors:
        if color.name.lower().startswith(char.lower()):
            return color
    return Color.NONE

def calc_all_questions(colors, positions):
    '''
    
    '''
    if positions <= 1:
        return colors
    lower_list = calc_all_questions(colors, positions-1)
    new_list = []
    for lower in lower_list:
        for color in colors:
            new_list.append(f"{color}{lower}")
    return new_list

def calc_answer(question, solution):
    '''
    
    '''
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

def random_question():
    questions = generate_all_questions(Colors, Positions)
    solution = random.choice(questions)
    question = random.choice(questions)
    answer = ask_question(question, solution)
    print(f"{question}: {answer} -- {solution}")

def best_question():
    questions = generate_all_questions(Colors, Positions)
    filtered = ["AABB", "ABAB", "GGGB", "GGGG", "AAAA", "BBBB", "BBAA"]
    best_question = ""
    best_value = 0
    for q in questions:
        value = calc_question_value(q, filtered)
        if value > best_value:
            best_question = q
            best_value = value
    print(f"Best question: {best_question} with value {best_value}")

def question_values():
    questions = generate_all_questions(Colors, Positions)
    for q in questions:
        value = calc_question_value(q, questions)
        print(f"{q=} {value=}")