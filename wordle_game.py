import numpy as np

class wordle:
    def __init__(self):
        with open('words.txt') as word_file:
            self.all_possible_words = list(word_file.read().split())
        self.word = np.random.choice(self.all_possible_words)
        self.guesses = [None] * 6
        self.all_info = np.zeros((6, 5), dtype='int')
        self.n_guesses = 0
        self.win = False

    def check_answer(self, correct_word, guess):
        info = np.zeros(5, dtype='int')
        for i in range(5):
            if correct_word[i] == guess[i]:
                info[i] = 2
            elif guess[i] in correct_word:
                info[i] = 1
        return info

    def make_guess(self, guess):
        if self.word == guess:
            self.win = True

        self.all_info[self.n_guesses] = self.check_answer(self.word, guess)
        self.guesses[self.n_guesses] = guess
        self.n_guesses += 1

        for j in range(len(self.all_possible_words) - 1, -1, -1):
            if not self.is_possible(self.all_possible_words[j], False):
                del self.all_possible_words[j]
    
    def is_possible(self, word, simulating):
        for i in range(self.n_guesses + simulating):
            for j in range(self.all_info.shape[1]):
                if self.all_info[i, j] == 2 and self.guesses[i][j] != word[j]:
                    return False
                if self.all_info[i, j] == 1 and (not self.guesses[i][j] in word or self.guesses[i][j] == word[j]):
                    return False
                if self.all_info[i, j] == 0 and self.guesses[i][j] in word:
                    return False

        return True