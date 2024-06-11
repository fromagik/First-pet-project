import time
from levenshtein import levenshtein
from data_base import *


#_____________________________ESPACE REGISTRATION______________________________

def registration_user():
    user_name_input = str(input('Enter your name: '))
    user_password_input = str(input("Enter your password: "))
    while True:
        if 1 <= len(user_name_input) <= 15 and len(user_password_input) >= 8:
            print('Registration successful')
            add_user(user_name_input, user_password_input) # Save user in database 
            break
        else:
            print('Please enter correct username and password or press "ENTER" to exit')
            user_name_input = str(input('Enter your name: '))
            user_password_input = str(input("Enter your password: "))
            if user_name_input == "" or user_password_input == "":
                main()

#_____________________________ESPACE USER_______________________________________

current_user = None #Create global user, we need for save current user 

def login():
    global current_user 
    user_name_input = str(input('Please enter your user name: '))
    user_password_input = str(input("Enter your password: "))
    if user_name_input and user_password_input:   
        while True:
            if not user_login(user_name_input, user_password_input):
                print('Wrong user name or password. For registration press "ENTER"')
                user_name_input = str(input('Please enter your user name: '))
                user_password_input = str(input("Enter your password: "))
                if user_name_input == "" or user_password_input == "":
                    registration_user()
            else:
                print("login successful")
                break
    if user_login(user_name_input, user_password_input): #if sign in are successful, save user 
        current_user = user_name_input
        return current_user


def show_records():
    global current_user
    records = get_all_records(current_user)
    if not records:
        user_menu()
    for record in records:
        print(record)
        user_menu()

#_______________________________ESPACE MENU_____________________________________

def main_menu():
    print('1: Register')
    print('2: Login')
    print('3: Exit')


def user_menu():
    print('1: Start game')
    print("2: Show records")
    print("3: Exit to main menu")
    while True: 
        choice = input('Make your choice: ')
        if choice == '1':
            start_game()
        elif choice == "2":
            show_records()
        elif choice == "3":
            main()
        else:
            print('Invalid choice')


def main():

    if not table_exist('game_data'):
        creat_table()

    while True:
        main_menu()
        choice = input("Make your choise: ")
        if choice == '1':
            registration_user()
        elif choice == '2':
            login()
            if current_user is not None:
                user_menu()
        elif choice == "3":
            break
        else:
            print('invalid choice. Try again')

#_______________________________ESPACE GAME_____________________________

def start_game():
    global current_user
    texts = ["\tThe quick brown fox jumps over the lazy dog.\n" 
            "This sentence is a classic example of a pangram, a sentence that uses every letter of the alphabet at least once.\n"
            "Typing pangrams is a great way to practice typing because they ensure you cover a wide range of letters and keystrokes.\v",

            "\tIn a small village by the sea, a young girl named Lily discovered a hidden cave filled with ancient treasures.\n"
            "She found gold coins, sparkling jewels, and mysterious maps.\n"
            "Excited by her discovery, Lily shared the news with her friends, and together they embarked on thrilling adventures that would change their lives forever.\v",

            "\tTechnology has revolutionized how we communicate, allowing people to connect instantly across the globe.\n"
            "Social media platforms enable us to share our lives, ideas, and experiences in real-time.\n"
            "However, it's crucial to balance screen time with face-to-face interactions to maintain strong personal relationships and mental well-being."]
    print('Welcome to the typing speed training game.')
    time.sleep(2)
    for ind, text in enumerate(texts):
        time.sleep(2)
        print(f'{ind}: {text}')
    user_chiose = int(input(f'Choose a text by selecting a number from 0 to {len(texts) - 1}. '))
    selected_text = texts[user_chiose]

    print("_" * 100)
    print(selected_text)
    print("_" * 100)
    time.sleep(2)
    print("START")
    start_time = time.time()
    user_input = str(input('>>>'))
    end_time = time.time()
    time_game = end_time - start_time # Time count  
    for char in selected_text:
        if char == '\n' or char == '\t' or char == "\v":
            selected_text = selected_text.replace(char, '') 
    errors = levenshtein(selected_text, user_input) # Count errors
    accuracy = (len(selected_text) - errors) / len(selected_text) * 100 # Count accuracy writing
    print(f'Time:{time_game}\nErrors:{errors}\nAccuracy: {accuracy}')
    set_user_achievement(current_user, time_game, accuracy) # Save user achievements in datebase 
    if time_game == get_time_records(current_user):
        print(f'You set a new record: {get_time_records(current_user)}')
    user_menu() # Return to user menu 

#__________________________START APPLICATION_______________
if __name__ == '__main__':
    main()




    