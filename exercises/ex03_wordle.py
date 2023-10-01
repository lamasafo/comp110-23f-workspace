"""EX03 - Structured Wordle."""

__author__ = "730478392"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, character: str)-> bool:
    """Searching for character in the word"""
    assert len(character)== 1
    index: int = 0
    while index < len(word):
        if word[index] == character:
            return True 
        index += 1
    return False

def emojified(word_guess: str, secret_word: str)-> str:
    """Determining if the guessed characters are in the secret word"""
    assert len(word_guess) == len(secret_word)
    guess_index: int = 0
    emoji: str = ""
    while guess_index < len(secret_word):
        if (word_guess[guess_index] == secret_word[guess_index]):
            emoji += GREEN_BOX
        else:
            if contains_char(secret_word, word_guess[guess_index]):
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        guess_index += 1
    return emoji 