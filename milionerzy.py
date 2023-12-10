import json
import question
JSON_FILE_USERS_DATABASE = "MyUsers.json"


def users_database_initialization():
    users_base = {"users_dane": []}
    with open(JSON_FILE_USERS_DATABASE, "w") as file:
        json.dump(users_base, file)


def user_record(users):
    dane_of_users = {"users_dane": users}
    with open(JSON_FILE_USERS_DATABASE, "w") as file:
        json.dump(dane_of_users, file, indent=3)


def add_new_user(username, password, email):
    my_user = load_user()
    new_users = {
        "username": username,
        "password": password,
        "email": email
    }
    my_user.append(new_users)
    user_record(my_user)


def load_user():
    try:
        with open("MyUsers.json", "r") as file:
            dane = json.load(file)
            return dane.get("users_dane", [])
    except (FileNotFoundError, json.JSONDecodeError):
        users_database_initialization()
        return []


def authorize_user(mail, password):
    users = load_user()
    for user in users:
        if user['email'] == mail and user['password'] == password:
            return True
    return False


def choice_in_first_menu():
    print("You have account?")
    print("1. Yes, I have account")
    print("2. No, I don't have account")
    print("3. Exit")
    while True:
        try:
            get_user_input = int(input("Your answer (1, 2, or 3): "))
            if get_user_input in [1, 2, 3]:
                return get_user_input
            else:
                print("Error: Please enter 1, 2, or 3.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def selection_authorization(choice1):
    while True:
        if choice1 == 1:
            mail = input('Enter your email address: ').strip()
            password = input('Enter your password: ')
            if authorize_user(mail, password):
                print('\nAuthorization was successful!')
                break
            else:
                print('\n| Invalid email address or password |\n')


def correct_username(username):
    while True:
        try:
            users = load_user()
            username_taken = False
            for user in users:
                if user['username'] == username:
                    print("| Username taken. Write a different username |")
                    username = input("Enter your new username: ")
                    username_taken = True
                    break
            if not username_taken:
                correct_username_in_def = username
                return correct_username_in_def
        except ValueError:
            print(" Error. Please try again.")


def correct_password(password):
    while True:
        try:
            if len(password) >= 8:
                correct_password_in_base = password
                return correct_password_in_base
            else:
                print("\n| Password is so small, try again. Minimum 8 characters |\n")
                password = str(input("Your password: "))
        except ValueError:
            print("|Error. Try again.|\n")


def selection_registration(choice2):
    if choice2 == 2:
        username = str(input("What is your username?: ")).strip()
        password = str(input("Your password: "))
        email = str(input("Your e-mail: ")).strip()
        correct_username_variable = correct_username(username)
        correct_password_variable = correct_password(password)

        while True:
            try:
                if email.count('@') == 1 \
                        and email.count('.') > 0 \
                        and email[0] != '@' \
                        and email.rfind('.') > email.rfind('@'):
                    correct_email_variable = email
                    break
                else:
                    print('| Invalid e-mail |\n')
                    email = str(input("Your e-mail: ")).strip()
            except ValueError:
                print("\n|Error|\n")
        add_new_user(correct_username_variable, correct_password_variable, correct_email_variable)
        print("\n!Added new user!")


def first_user_selection_menu():
    choice = choice_in_first_menu()
    if choice == 1:
        selection_authorization(choice)
    elif choice == 2:
        selection_registration(choice)
    elif choice == 3:
        print("Ok, goodbye!")
        exit()


def present_game_menu():
    print("1. Lets go Play")
    print("2. Quit")
    while True:
        try:
            get_user_input = int(input("Your answer: "))
            if get_user_input in [1, 2]:
                return get_user_input
            else:
                print("Error answer!")
        except ValueError:
            print("Error. Please try again.")


def game_menu():
    while True:
        try:
            choice_in_game_menu = present_game_menu()
            if choice_in_game_menu == 1:
                question.play_millionaire()
            else:
                print("Ok, goodbye!")
                exit()
        except ValueError:
            print("Error. Please try again.")


if __name__ == "__main__":
    my_list = \
        ["Welcome to the game 'Millionaire'!!!", "To continue, register or log in!",
            "Please select the correct option!\n"]
    for _ in range(3):
        print(my_list[_])
    first_user_selection_menu()
    game_menu()
