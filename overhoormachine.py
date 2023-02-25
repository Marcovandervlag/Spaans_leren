import random

#This function will read the .txt file with the words in it. The file is build up like this:
# english word, spanish word,category
#For example:
# cheese,queso,food
#After reading it will sort out the category and will return the words that are in that specific category.
def load_words(category):
    with open('.\spanish_words.txt', 'r', encoding='utf-8') as f:
        words = [line.strip().split(',') for line in f.readlines()]
    if category:
        words = [w for w in words if w[2] == category]
    return words

#This function is the menu option you will get after starting the program.
#It will let you choose between the categories given in the list below.
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
        print("10. Days")
        print("11. Months")
        print("12. Vervoeging")
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
        elif choice == '10':
            return 'Days'
        elif choice == '11':
            return 'Months'
        elif choice == '12':
            return 'vervoeging'
        else:
            print("Invalid choice, please try again.")
#Makes all the words random. So there is (Almost) never the same quiz.
def get_word(words):
    return random.choice(words)

#This function will get the word of the translation and ask you what is the translation off it
def translate(word):
    english_word, spanish_word, category = word
    guess = input(f"What is the Spanish word for {english_word}? ")
    return guess.lower() == spanish_word.lower()

#This function will start de quiz/game and will gather all the correct answers and 
#all the answers that you filled in incorrect.
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

#This will start the whole program.
if __name__ == '__main__':
    category = get_category()
    play_game(category)
