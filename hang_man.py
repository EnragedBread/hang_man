import math
import random
from string import ascii_lowercase

import word_file

DEFAULT_WORD = "pneumonoultramicroscopicsilicovolcanoconiosis"
GALLOWS = [
'''
 |--|
 |  0
 | \|/
 |  |
 | / \\
_|_
''',
'''
 |--|
 |  0
 | \|/
 |  |
 | /
_|_
''',
'''
 |--|
 |  0
 | \|/
 |  |
 |
_|_
''',
'''
 |--|
 |  0
 | \|/
 |
 |
_|_
''',
'''
 |--|
 |  0
 | \|
 |
 |
_|_
''',
'''
 |--|
 |  0
 |  |
 |
 |
_|_
''',
'''
 |--|
 |  0
 |
 |
 |
_|_
''',
'''
 |--|
 |
 |
 |
 |
_|_
''',
]

def display_word(word, correct_letters):
    obscured_word = word
    alphabet = set(ascii_lowercase)
    incorrect_letters = alphabet - correct_letters

    for letter in incorrect_letters:
        obscured_word = obscured_word.replace(letter, "_")
    return " ".join(obscured_word)

if __name__ == "__main__":
    """
    word_list: The list of possible words that the game can use.
    word: Current Word being used.
    word_letters: The unordered collection of all letters used in the word (not including duplicates).
    correct_guesses: Correctly guessed letters (including pre-guessed letters).
    letters_remaining: Correct letters that haven't been guessed yet.

    incorrect_guesses: All of your guesses that aren't in the word.
    all_guesses: Every letter guessed (right or wrong).
    """
    print(f"Welcome to Hang Man!")

    custom_file = input(f"Do you have a custom word list you would like to use? Enter the name here (must be a .txt file!): ").strip()

    try:
        word_list = word_file.load_words(custom_file)
    except word_file.WordListError:
        try:
            word_list = word_file.load_words('default.txt')
        except word_file.WordListError:
            print(f"Sorry I was unable to load the Word List!")
            word_list = [DEFAULT_WORD]

    word = word_list[random.randint(0, len(word_list) - 1)].lower()
    whitelist = set(ascii_lowercase)
    word_letters = set()
    for letter in word:
        if letter in whitelist:
            word_letters.add(letter)

    num_to_start = math.floor(0.25*len(word_letters))
    correct_guesses = set(random.sample(word_letters, num_to_start))
    incorrect_guesses = set()

    all_guesses = correct_guesses

    letters_remaining = word_letters - correct_guesses

    life_left = 7

    while len(letters_remaining) > 0 and life_left:
        so_far = display_word(word, correct_guesses)

        print(GALLOWS[life_left])
        print(f"\nYour life total is currently at: {life_left}")
        print(f"\nPrint the rest of the missing letters to finish the word (in all lowercase) {so_far}")
        print(f"\nHere are all of your previous incorrect guesses! ---[{' '.join(incorrect_guesses)}]---")

        letter_choice = input(f"\nWhat letter do you wish to guess? ").lower().strip()

        if letter_choice in letters_remaining:
            correct_guesses.add(letter_choice)
            letters_remaining.discard(letter_choice)
            print(f"\nYou guessed right! You didn't lose any life this round!")

        elif letter_choice in all_guesses:
            print(f"\nYou have already guessed that letter!")

        else:
            life_left -= 1
            incorrect_guesses.add(letter_choice)
            print(f"\nYou guessed wrong, you lost a life!")

        all_guesses.add(letter_choice)

    print(GALLOWS[life_left])
    print(f"Here is the finalized word! {word}")
    if life_left:
        print(f"\nYou win!!!")
    else:
        print(f"\nYou ran out of life! try again next time.")