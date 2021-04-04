import random

def new_game():

    print("Do you wanna play again?(Type 'yes' or 'no')")
    new_game = input("type here: ")
    if new_game == 'yes':
        game()
    else:
        print("Thank you, bye.")

def game():

    file = open('ak_words', 'r', encoding='utf-8')
    word_list = list(file)
    file.close()
    word = "".join(random.choice(word_list))
    word = word.replace(word[-1], "").lower()
    word = list(word)
    #print("".join(word))
    underline = "".join([i.replace(i, "_") for i in word])
    underline = list(underline)
    print("".join(underline))
    wrong_letters = []
    tips = 20

    while word != underline:

        letter = input('Give a letter: ').lower()
        if len(letter) != 1:
            print("One letter error.\n")

        if letter in wrong_letters:

            print("Tried earlier: ", letter)
            print("Tried letters: ", wrong_letters)
            print("The word: ", ''.join(underline))
            print(" ")

        else:

            if letter in word:
                underline = list(underline)
                where = [i for i in range(len(word)) if word[i] == letter]
                for i in where:
                    underline[i] = letter

                print("Word: ", "".join(underline))
                print("Tips left: ", tips)
                print(" ")


            elif letter not in word:
                tips -= 1
                wrong_letters.append(letter)
                print("Not in the word: ", wrong_letters)
                print("Tips left: ", tips)
                print("The word: ", "".join(underline))
                print(" ")

                if tips < 1:
                    print("You're out of tips... ")
                    print("The word was: ", "".join(word))
                    new_game()


    print("Congratulation! You won! The word was:", "".join(word))
    print("")
    new_game()


game()
