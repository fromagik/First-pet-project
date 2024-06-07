import time 

def levenshtein(s1, s2):
    n, m = len(s1), len(s2)
    if n > m:
        m, n = n, m
        s1, s2 = s2, s1

    curr_row = range(n + 1)
    for i in range(1, m + 1):
        prev_row, curr_row = curr_row, [i] + [0] * n
        for j in range(1, n + 1):
            inser = prev_row[j] + 1
            delet = curr_row[j - 1] + 1
            subs = prev_row[j - 1] + (s1[j - 1] != s2[i - 1])
            curr_row[j] = min(inser, delet, subs)
    
    return curr_row[n]

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



if __name__ == '__main__':
    start_game()




    