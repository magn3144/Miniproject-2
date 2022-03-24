from wordle_game import wordle

env = wordle()
n_impossible_words = 0
for word in env.all_possible_words:
    if not env.is_possible(word, True):
        n_impossible_words += 1