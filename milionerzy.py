import json
import random
JSON_FILE_USERDATABASE = "MyUsers.json"
# Klasa reprezentująca pytanie
class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

# Lista pytań
questions = [
    Question("Jaki jest stolica Francji?", ["A. Berlin", "B. Madryt", "C. Paryż", "D. Londyn"], "C"),
    Question("Który gaz jest najbardziej obfity w atmosferze Ziemi?", ["A. Azot", "B. Tlen", "C. Wodór", "D. Hel"], "A"),
    Question("Ile wynosi 2 do potęgi 5?", ["A. 16", "B. 32", "C. 64", "D. 128"], "B"),
    # Dodaj więcej pytań według potrzeб
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

# Funkcja sprawdzająca, czy odpowiedź jest poprawна
def check_answer(question, user_answer):
    return user_answer == question.correct_option

# Funkcja główna gry
def play_millionaire(questions):
    score = 0
    for _ in range(15):  # Gracz ma 15 pytań do odpowiedzenia
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

def inicjalizuj_baze_danych():
    UsersBase = {"users_dane": []}
    with open(JSON_FILE_USERDATABASE, "w") as file:
        json.dump(UsersBase, file)

def zapisz_produkty(users):
    dane_of_users = {"users_dane": users}
    with open(JSON_FILE_USERDATABASE, "w") as file:
        json.dump(dane_of_users, file, indent=3)

def add_new_user(User_name, Password, Mail):
    MyUser = load_user()
    new_users = {
        "Username": User_name,
        "Password": Password,
        "E-Mail": Mail
    }
    MyUser.append(new_users)
    zapisz_produkty(MyUser)

def load_user():
    try:
        with open("MyUsers.json", "r") as file:
            dane = json.load(file)
            return dane.get("users_dane", [])
    except (FileNotFoundError, json.JSONDecodeError):
        inicjalizuj_baze_danych()
        return []

def authorize_user(mail, password):
    users = load_user()
    for user in users:
        if user['E-Mail'] == mail and user['Password'] == password:
            return True
    return False

def wybor():
    print("You have account?")
    print("1. Yes, I have account")
    print("2. No, I don't have account")
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
def wybor_1(wybor1):
    while True:
        if wybor1 == 1:
            mail = input('Enter your email address: ').strip()
            password = input('Enter your password: ')
            if authorize_user(mail, password):
                print('\nAuthorization was successful!')
                break
            else:
                print('\n| Invalid email address or password |\n')
def correct_username(User_name):
    while True:
        try:
            users = load_user()
            username_taken = False
            for user in users:
                if user['Username'] == User_name:
                    print("| Username taken. Write a different username |")
                    User_name = input("Enter your new username: ")
                    username_taken = True
                    break
            if not username_taken:
                CorrectUsername = User_name
                return CorrectUsername
        except ValueError:
            print("Error. Please try again.")
def correct_password(Password):
    while True:
        try:
            if len(Password) >= 8:
                correct_password_in_base = Password
                return correct_password_in_base
            else:
                print("\n| Password is so small, try again. Minmum 8 characters |\n")
                Password = str(input("Your password: "))
        except ValueError:
            print("|Error. Try again.|\n")
def wybor_2(wybor2):
    if wybor2 == 2:
            User_name = str(input("What is your username?: ")).strip()
            Password = str(input("Your password: "))
            Mail = str(input("Your e-mail: ")).strip()
            CorrectUsername = correct_username(User_name)
            CorrectPassword = correct_password(Password)

            while True:
                try:
                    if Mail.count('@') == 1 \
                            and Mail.count('.') > 0 \
                            and Mail[0] != '@' \
                            and Mail.rfind('.') > Mail.rfind('@'):
                        CorrectMail = Mail
                        break
                    else:
                        print('| Invalid e-mail |\n')
                        Mail = str(input("Your e-mail: ")).strip()
                except ValueError:
                    print("\n|Error|\n")
            add_new_user(CorrectUsername, CorrectPassword, CorrectMail)
            print("\n!Added new user!")

def first_user_selection_menu():
    wybor1 = wybor()
    if wybor1 == 1:
        wybor_1(wybor1)
    elif wybor1 == 2:
        wybor_2(wybor1)


if __name__ == "__main__":
    print('''\n!!!Welcome to the game "Millionaire"!!!\n
   To continue, register or log in! 
   Please select the correct option!\n''')
    first_user_selection_menu()
