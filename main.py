# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
import numpy as np


def hangman():
    response_api = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    text = response_api.text
    j_text = json.loads(text)[0]
    # selecting hints according to the number of letter in the word.
    length_of_text = len(j_text)
    if (length_of_text < 6):
        no_of_letters = 2
    elif (length_of_text < 9):
        no_of_letters = 3
    elif (length_of_text < 11):
        no_of_letters = 4
    else:
        no_of_letters = 5

    # selecting random positions of the hints. 
    values = np.random.randint(0, length_of_text, size=no_of_letters)
    # just a copy of original text/word
    duplicate_text = j_text
    # list of already present characters as hint
    present_letters_list = []
    
    # this for loop is used to convert the letters at the position 
    # other than the letters at randomly selected position to _
    for i in range(0, length_of_text):
        if i not in values:
            duplicate_text = duplicate_text.replace(duplicate_text[i], '_', 1)
        else:
            present_letters_list.append(duplicate_text[i])
    # print(values)

    run_hangman_game(duplicate_text, j_text, present_letters_list, values)


def run_hangman_game(converted_text, original_text, ava_words, positions):
    print(converted_text)
    # print(ava_words)
    life_count = 5
    
    # list of total number of characters in the text
    words_list = split(original_text)
    # print(words_list)
    
    # remove the already available characters as a hint from the list.
    remaining_char = split_list(words_list, positions)
    # print(remaining_char)
    while True:

        if (life_count == 0):
            print('OOPS... You lost The Game')
            print('The correct answer was : ', original_text)
            break
        elif (converted_text == original_text):
            print('Hurray... You Won The Game..Congratulation')
            break
        else:
            inp = input('guss a word')
            if inp in remaining_char:
                # converting all presence of the typed words from _ to word
                for i in range(len(words_list)):
                    if inp == words_list[i]:
                        converted_text = converted_text[:i] + inp + converted_text[i + 1:]
                remaining_char.remove(inp)
                print(converted_text)
            else:
                life_count -= 1
                print('lost a life, remaining lifes are ', life_count)
                print(converted_text)


def split(word):
    return [word for word in word]


def split_list(l1, pos):
    l2 = []
    for i in range(len(l1)):
        if i not in pos:
            l2.append(l1[i])
    return l2


# no of letters to show
# convert the other letters to _


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    hangman()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
