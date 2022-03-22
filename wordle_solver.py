from wordle_game import wordle
import numpy as np

def solve_wordle():
    env = wordle()
    all_info = np.full((6, 5), -1)
    for i in range(6):
        information_gain_sums = np.zeros(len(env.all_possible_words), dtype='int')
        for j, possible_guess in enumerate(env.all_possible_words):
            for possible_word in env.all_possible_words:
                env.guesses[env.n_guesses] = possible_guess
                env.all_info[env.n_guesses] = env.check_answer(possible_word, possible_guess)
                n_impossible_words = 0
                for word in env.all_possible_words:
                    if not env.is_possible(word, True):
                        n_impossible_words += 1
                information_gain_sums[j] += n_impossible_words
        env.make_guess(env.all_possible_words[np.argmax(information_gain_sums)])
        for j in range(len(env.all_possible_words) - 1, -1, -1):
            if not env.is_possible(env.all_possible_words[j], False):
                del env.all_possible_words[j]
        print(env.guesses[i])
        print(len(env.all_possible_words))

if __name__ == '__main__':
    solve_wordle()