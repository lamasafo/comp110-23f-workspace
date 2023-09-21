"""EX02 - One Shot Wordle."""

__author__ = "730478392"
secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Ask them to guess a 6-letter word
word_guess: str = str(input(f"What is your {len(secret_word)}-letter guess? "))
# If word is not 6 letters, tell them
while len(word_guess) != len(secret_word):
    print(f"That was not {len(secret_word)} letters! ")
    word_guess: str = input("Try again: ")


secret_index: int = 0
guess_index: int = 0

result_string: str = ""

while secret_index < len(secret_word):
    if secret_word[secret_index] == word_guess[secret_index]:
        result_string += GREEN_BOX
    else:
        check: bool = False
        guess_index: int = 0
        while not(check) and guess_index < len(secret_word):
            if secret_word[guess_index] == word_guess[secret_index]:
                check = True
            guess_index += 1 
        if check:
            result_string += YELLOW_BOX
        else:
            result_string += WHITE_BOX

    secret_index += 1 
    
# If guess word is correct, congratulate them.
if word_guess == secret_word:
    print(f"{result_string} ")
    print("Woo! You got it! ")
# If word is not correct, tell them.
else:
    print(f"{result_string}")
    print("Not quite. Play again soon! ")