import math
import random

import word_file

def display_word(word, correct_letters):
    obscured_word = word
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    incorrect_letters = alphabet - correct_letters

    for letter in incorrect_letters:
        obscured_word = obscured_word.replace(letter, "_")
    return " ".join(obscured_word)

if __name__ == "__main__":
    print(f"Welcome to Hang Man!")

    life_left = 7

    try:
        word_list = word_file.load_words('default.txt')
    except word_file.WordListError:
        print(f"Sorry I was unable to load the Word List!")
        word_list = ["pneumonoultramicroscopicsilicovolcanoconiosis"]

    word = word_list[random.randint(0, len(word_list) - 1)].lower()
    word_letters = set(word)
    num_to_start = math.floor(0.25*len(word_letters))
    correct_guesses = set(random.sample(word_letters, num_to_start))

    letters_remaining = set(word) - correct_guesses

    while len(letters_remaining) > 0 and life_left:
        so_far = display_word(word, correct_guesses)

        print(f"\nPrint the rest of the missing letters to finish the word (in all lowercase) {so_far}")

        letter_choice = input(f"\nWhat letter do you wish to guess? ").lower().strip()

        if letter_choice in letters_remaining:
            correct_guesses.add(letter_choice)
            letters_remaining.discard(letter_choice)
            so_far = display_word(word, correct_guesses)
            print(f"\nYou guessed right! Here is your updated word: {so_far}")

        else:
            life_left -= 1
            print(f"\nYou guessed wrong, you lost a life!")

        print(f"\nYour life total is currently at: {life_left}")

    if life_left:
        print(f"\nYou win!!!")
    else:
        print(f"\nYou ran out of life! try again next time.")