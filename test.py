from wordle_game import wordle

env = wordle()
env.make_guess("ching")
n_impossible_words = 0
for word in env.all_possible_words:
    if not env.is_possible(word, False):
        n_impossible_words += 1

print(n_impossible_words)