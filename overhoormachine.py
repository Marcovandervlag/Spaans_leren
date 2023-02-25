import random

def load_words(category):
    with open('.\spanish_words.txt', 'r', encoding='utf-8') as f:
        words = [line.strip().split(',') for line in f.readlines()]
    if category:
        words = [w for w in words if w[2] == category]
    return words

def get_category():
    while True:
        print("Select a category:")
        print("1. Korfball")
        print("2. Food")
        print("3. Drink")
        print("4. Hobbies")
        print("5. greetings")
        print("6. Looks")
        print("7. Colors")
        print("8. Weather")
        print("9. objects")
        choice = input()
        if choice == '1':
            return 'Korfball'
        elif choice == '2':
            return 'Food'
        elif choice == '3':
            return 'Drink'
        elif choice == '4':
            return 'Hobbies'
        elif choice == '5':
            return 'Greetings'
        elif choice == '6':
            return 'Looks'
        elif choice == '7':
            return 'Colors'
        elif choice == '8':
            return 'Weather'
        elif choice == '9':
            return 'Objects'
        else:
            print("Invalid choice, please try again.")

def get_word(words):
    return random.choice(words)

def translate(word):
    english_word, spanish_word, category = word
    guess = input(f"What is the Spanish word for {english_word}? ")
    return guess.lower() == spanish_word.lower()

def play_game(category=None):
    words = load_words(category)
    correct = 0
    total = 0
    while True:
        word = get_word(words)
        if translate(word):
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is {word[1]}")
        total += 1
        if total == 10:
            break
    print(f"Game over! You scored {correct} out of {total}.")

if __name__ == '__main__':
    category = get_category()
    play_game(category)
