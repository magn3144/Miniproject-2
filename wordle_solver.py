from wordle_game import wordle
import numpy as np

def solve_wordle():
    env = wordle()
    env.make_guess("raise")
    print(len(env.all_possible_words))
    for i in range(5):
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
        if i == 0:
            with open("output.txt", 'w') as f:
                f.write(env.guesses[i])
        print(env.guesses[i])
        print(len(env.all_possible_words))

if __name__ == '__main__':
    solve_wordle()