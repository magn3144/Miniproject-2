import numpy as np

class wordle:
    def __init__(self):
        self.word = np.random.choice(self.load_words())

    def load_words(self):
        with open('wordlist.txt') as word_file:
            return list(word_file.read().split())
    
    def make_guess(self, guess):
        info = []
        for letter_self, letter_guess in zip(self.word, guess):
            if letter_self == letter_guess:
                info.append(2)
            elif letter_guess in self.word:
                info.append(1)
            else:
                info.append(0)
        return info