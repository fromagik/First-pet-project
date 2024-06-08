import time
from levenshtein import levenshtein
from data_base import creat_table, table_exist, add_user, user_login


def main_menu():
    print('1: Register')
    print('2: Login')
    print('3: Exit')

def registration_user():
    user_name_input = str(input('Enter your name: '))
    user_password_input = str(input("Enter your password: "))
    while True:
        if 1 < user_name_input > 15 and user_password_input <= 8:
            print('Registration successful')
            add_user(user_name_input, user_password_input)
            break
        else:
            print('Please enter corect username and password.')

def login():
    user_name_input = str(input('Please enter your user name: '))
    user_password_input = str(input("Enter your password: "))
    if user_name_input and user_password_input:
        count = 0
        while count != 3:
            if not user_login(user_name_input, user_password_input):
                count += 1
                print('Wrong user name or password')
                user_name_input = str(input('Please enter your user name: '))
                user_password_input = str(input("Enter your password: "))
            else:
                print("login successful")
                return True
        return False
        
        



def start_game():
    texts = ["Hello","In a small village by the sea, a young girl named Lily discovered a hidden cave filled with ancient treasures. She found gold coins, sparkling jewels, and mysterious maps. Excited by her discovery, Lily shared the news with her friends, and together they embarked on thrilling adventures that would change their lives forever.","Technology has revolutionized how we communicate, allowing people to connect instantly across the globe. Social media platforms enable us to share our lives, ideas, and experiences in real-time. However, it's crucial to balance screen time with face-to-face interactions to maintain strong personal relationships and mental well-being."]
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
    start_time = time.time()
    print("START")
    user_input = str(input('>>>'))
    end_time = time.time()
    time_game = end_time - start_time
    errors = levenshtein(selected_text, user_input)
    print(f'Time:{time_game}\nErrors:{errors}\nAccuracy: {((len(selected_text) - errors ) / len(selected_text)) * 100}')

def main():

    if not table_exist('game_data'):
        creat_table()

    while True:
        main_menu()
        choice = input("your choise: ")
        if choice == '1':
            registration_user()
        elif choice == '2':
            if login():
                start = input("You wann to start game? y/n: ")
                if start == 'y':
                    start_game()
                else:
                    continue
        elif choice == "3":
            break
        else:
            print('invalide choice. try again')

if __name__ == '__main__':
    main()




    