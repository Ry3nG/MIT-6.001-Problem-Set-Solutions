import string


def is_word_guessed(secret_word, letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    output = [char for char in secret_word]
    for i in range(len(secret_word)):
        if secret_word[i] not in letters_guessed:
            output[i] = "_"
    return "".join(output)


def get_available_letters(letters_guessed):
    all_letters = [char for char in string.ascii_lowercase]
    return_list = []
    for element in all_letters:
        if element not in letters_guessed:
            return_list.append(element)
    return "".join(return_list)


def match_with_gaps(my_word, other_word):
    i = 0
    used_characters = []
    if len(my_word)!=len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != "_" and my_word[i] != other_word[i]:
                return False
            elif my_word[i] != "_" and my_word[i] == other_word[i]:
                used_characters.append(my_word[i])
            elif my_word[i] == "_" and other_word[i] in used_characters:
                return False
            elif my_word[i] == '_' and other_word[i] not in used_characters:
                pass
            else:
                print("Error in cases!")

    return True
# test case

print(match_with_gaps("te_t", "tact"))  # False
print(match_with_gaps("a__le", "apple"))  # True
print(match_with_gaps("ap_le", "apple"))  # False
