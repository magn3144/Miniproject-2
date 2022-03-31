from wordle_game import wordle
import numpy as np
import time

def solve_wordle(env):
    env.make_guess("raise")
    if env.win:
        print(f"AI won in 1 guess")
    for i in range(5):
        # print("AI guessed: " + env.guesses[i])
        # print("Words left: " + str(len(env.all_possible_words)))
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
        if env.win:
            print("AI guessed the correct word: " + env.guesses[i + 1])
            print(f"AI won in {i + 2} guesses")
            break
        if i == 0:
            with open("output.txt", 'w') as f:
                f.write(env.guesses[i])

if __name__ == '__main__':
    with open('words_to_guess.txt') as word_file:
        words = list(word_file.read().split())
    for i in range(10):
        print(f"---Round {i + 1}---")

        # env = wordle()
        # env.word = words[i]
        # for j in range(6):
        #     env.make_guess(input())
        #     print(env.all_info[j])
        #     if env.win:
        #         print("Player won in " + str(j + 1) + " guesses")
        #         break

        start_time = time.perf_counter()
        env = wordle()
        env.word = words[i]
        solve_wordle(env)
        end_time = time.perf_counter()
        delta_t = np.round(end_time - start_time, 2)
        print(f"Total time: {delta_t}")

        with open('guess_times.txt', 'a') as f:
            f.write(f"{words[i]}:{' '*(12 - (len(str(delta_t)) + len(words[i])))}{delta_t}\n")