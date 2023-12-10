import json
import random
import milionerzy
JSON_FILE_QUESTIONS = "questions.json"
SCORE = 0


class Questions:
    def __init__(self, question):
        self.question = question

    def output(self):
        print(f"Question for {self.question}$")

    def present_question(self, question):
        global SCORE
        print(question["question"])
        for option in question["answer_options"]:
            print(option)
        user_answer = input(" Choose an answer (e.g., 'A'): ").upper()
        while True:
            try:
                if user_answer in ["A", "B", "C", "D"]:
                    return user_answer
            except ValueError:
                print("Write correct answer")
                user_answer = input("Choose an answer (e.g., 'A'): ").upper()
            else:
                print("Write correct answer")
                user_answer = input("Choose an answer (e.g., 'A'): ").upper()


def initialize_database():
    questions_base = {"users_dane": []}
    with open(JSON_FILE_QUESTIONS, "w") as file:
        json.dump(questions_base, file)


def load_user():
    try:
        with open(JSON_FILE_QUESTIONS, "r") as file:
            dane = json.load(file)
            return dane.get("questions", [])
    except (FileNotFoundError, json.JSONDecodeError):
        initialize_database()
        return []


def get_random_question():
    questions = load_user()
    if len(questions) == 0:
        return None

    random_index = random.randint(0, len(questions) - 1)
    question = questions[random_index]

    questions.pop(random_index)

    return question


def check_answer(question, user_answer):
    return user_answer == question["correct_answer"]


def present_leave_menu():
    print("1. Next Question")
    print("2. Leave and take money")
    get_user_input = int(input("Your answer: "))
    while True:
        try:
            if get_user_input in [1, 2]:
                return get_user_input
            else:
                print("Error answer!")
                get_user_input = int(input("Your answer: "))
        except ValueError:
            pass


def play_millionaire():
    global SCORE
    amount_money = 100
    step_first_lvl = 100
    for _ in range(4):
        obj = Questions(amount_money)
        question = get_random_question()
        if question is not None:
            obj.output()
            user_answer = obj.present_question(question)
            if check_answer(question, user_answer):
                print(" Correct! ")
                SCORE += 1
                choice_leave_or_next = present_leave_menu()
                if choice_leave_or_next == 2:
                    print(f"You won {amount_money}$! Good luck!")
                    exit()
            else:
                print(" Wrong answer. Game over.")
                return
        amount_money = amount_money + step_first_lvl

    step_second_lvl = 2
    for _ in range(8):
        obj = Questions(amount_money)
        question = get_random_question()
        if question is not None:
            obj.output()
            user_answer = obj.present_question(question)
            if check_answer(question, user_answer):
                print("Correct!\n")
                SCORE += 1
                if SCORE == 6:
                    print("Your guaranteed amount is $1000")
                if SCORE == 11:
                    print("Your guaranteed amount is $32000")
                choice_leave_or_next = present_leave_menu()
                if choice_leave_or_next == 2:
                    print(f"You won {amount_money}$! Good luck!")
                    exit()
            else:
                print("Wrong answer. Game over.")
                if 6 <= SCORE < 11:
                    print("You withdraw your guaranteed winnings of $1000! Good luck!")
                if 11 <= SCORE < 15:
                    print("You withdraw your guaranteed winnings of $32000! Good luck!")
                return
        amount_money = amount_money * step_second_lvl

    amount_money = amount_money - 3000
    step_third_lvl = 2
    for _ in range(4):
        obj = Questions(amount_money)
        question = get_random_question()
        if question is not None:
            obj.output()
            user_answer = obj.present_question(question)
            if check_answer(question, user_answer):
                print("Correct!\n")
                SCORE += 1
                if SCORE == 16:
                    print("Congratulations, you answered all the questions! You are a millionaire!")
                    return
                choice_leave_or_next = present_leave_menu()
                if choice_leave_or_next == 2:
                    print(f"You won {amount_money}$! Good luck!")
                    exit()
            else:
                print("Wrong answer. Game over.")
                if 11 <= SCORE < 15:
                    print("You withdraw your guaranteed winnings of $32000! Good luck!")
                return
        amount_money = amount_money * step_third_lvl


if __name__ == "__main__":
    print("Welcome to the game 'Who Wants to Be a Millionaire?'")
    play_millionaire()
