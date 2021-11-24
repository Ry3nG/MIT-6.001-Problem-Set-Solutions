def is_word_guessed(secret_word, letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True


# test case
secret_word = "apple"
letters_guessed = ["i", "e", "l", "p", "p", "a"]
print(is_word_guessed(secret_word, letters_guessed))
