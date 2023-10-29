import random


def millionaire_game():
    questions = {
        "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
        "What is the largest planet in our solar system?": ["Jupiter", "Saturn", "Mars", "Venus"],
        "What is the smallest country in the world?": ["Vatican City", "Monaco", "Nauru", "Tuvalu"],
        "What is the highest mountain in the world?": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "What is the largest ocean in the world?": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Southern Ocean"]
    }

    correct_answers = {
        "What is the capital of France?": 0,
        "What is the largest planet in our solar system?": 0,
        "What is the smallest country in the world?": 0,
        "What is the highest mountain in the world?": 0,
        "What is the largest ocean in the world?": 0
    }

    prize_money = {
        1: "$100",
        2: "$200",
        3: "$300",
        4: "$500",
        5: "$1,000",
        6: "$2,000",
        7: "$4,000",
        8: "$8,000",
        9: "$16,000",
        10: "$32,000",
        11: "$64,000",
        12: "$125,000",
        13: "$250,000",
        14: "$500,000",
        15: "$1,000,000"
    }

    question_number = 1
    prize_money_won = ""

    while question_number <= len(questions):
        print(f"Question {question_number}:")

        question = random.choice(list(questions.keys()))

        print(question)

        for i in range(len(questions[question])):
            print(f"{i + 1}. {questions[question][i]}")

        answer = input("Enter your answer (1-4): ")

        if int(answer) - 1 == correct_answers[question]:
            print("Correct!")

            if question_number == len(questions):
                prize_money_won = prize_money[question_number]
                break

            question_number += 1
            prize_money_won = prize_money[question_number]

            del questions[question]
            del correct_answers[question]

            print(f"You have won {prize_money_won}!")

            continue

        print("Incorrect. Game over.")

        break

    print(f"You won {prize_money_won}!")
    print(f"You FUCKING WON {prize_money_won}!")