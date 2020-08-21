import os

class WordListError(Exception):
    pass

def load_words(file_name):
    here = os.path.dirname(os.path.abspath(__file__))
    word_file = os.path.join(here, "wordlists", file_name)

    words = []
    try:
        with open(word_file, 'r') as file_object:
            for line in file_object:
                words.append(line.strip())

    except (IOError, FileNotFoundError) as e:
        raise WordListError(e)

    return words