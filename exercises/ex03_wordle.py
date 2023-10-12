"""EX03 - Structured Wordle."""

__author__ = "730478392"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """Searching for character in the word."""
    assert len(character) == 1
    index: int = 0
    while index < len(word):
        if word[index] == character:
            return True 
        index += 1
    return False


def emojified(word_guess: str, secret_word: str) -> str:
    """Determining if the guessed characters are in the secret word."""
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


def input_guess(expected_length: int) -> str:
    """Telling user to input the right number of characters."""
    word: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(word):
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    guess_index: int = 1
    secret_word: str = "codes"
    word_guess: str = ""
    turns: int = 6
    while guess_index <= turns and word_guess != secret_word:
        print(f"=== Turn {guess_index}/{turns} ===")
        word_guess = input_guess(len(secret_word))
        print(emojified(word_guess, secret_word))
        if word_guess == secret_word:
            print(f"You won in {guess_index}/{turns} turns!")
        else:
            guess_index += 1
    if word_guess != secret_word:
        print(f"X/{turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
