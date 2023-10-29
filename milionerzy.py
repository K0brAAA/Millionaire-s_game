import random


# Klasa reprezentująca pytanie
class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option


# Lista pytań
questions = [
    Question("Jaki jest stolica Francji?", ["A. Berlin", "B. Madryt", "C. Paryż", "D. Londyn"], "C"),
    Question("Który gaz jest najbardziej obfity w atmosferze Ziemi?", ["A. Azot", "B. Tlen", "C. Wodór", "D. Hel"],
            "A"),
    Question("Ile wynosi 2 do potęgi 5?", ["A. 16", "B. 32", "C. 64", "D. 128"], "B"),
    # Dodaj więcej pytań według potrzeb
]


# Funkcja losująca pytanie
def select_random_question(questions):
    return random.choice(questions)


# Funkcja prezentująca pytanie i opcje odpowiedzi
def present_question(question):
    print(question.text)
    for option in question.options:
        print(option)
    user_answer = input("Wybierz odpowiedź (np. 'A'): ").upper()
    return user_answer


# Funkcja sprawdzająca, czy odpowiedź jest poprawna
def check_answer(question, user_answer):
    return user_answer == question.correct_option


# Funkcja główna gry
def play_millionaire(questions):
    score = 0

    for i in range(15):  # Gracz ma 15 pytań do odpowiedzenia
        question = select_random_question(questions)
        user_answer = present_question(question)

        if check_answer(question, user_answer):
            score += 1
            print("Odpowiedź poprawna!\n")
        else:
            print("Niestety, odpowiedź nieprawidłowa. Koniec gry.")
            break

    if score == 15:
        print("Gratulacje! Wygrałeś milion złotych!")
    else:
        print("Zdobyłeś {} złotych. Dziękujemy za udział w grze.".format(1000 * score))


if __name__ == "__main__":
    play_millionaire(questions)
