SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}
def get_word_score(word, n):
    wordLower = word.lower()
    wordLen = len(wordLower)
    score = 0
    for character in wordLower:
        score += SCRABBLE_LETTER_VALUES[character]
    if (7 * wordLen - 3 * (n - wordLen)) > 1:
        score *= 7 * wordLen - 3 * (n - wordLen)
    else:
        score*= 1

    return score

print(get_word_score("it", 7))