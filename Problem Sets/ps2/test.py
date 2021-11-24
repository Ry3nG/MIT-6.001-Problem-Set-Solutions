def is_word_guessed(secret_word, letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    output = [char for char in secret_word]
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            output[i] ='_'
    return "".join(output)


# test case
secret_word = "apple"
letters_guessed = ["e",'i','k','p','r', 's']
print(get_guessed_word(secret_word, letters_guessed))
