"""Dictionary Practice!"""

_author_ = "730478392"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the key value pairs in a dictionary."""
    output: dict[str, str] = dict()
    for key, value in dictionary.items():
        output[value] = key
        if value in output.keys():
            raise KeyError
    return output


def favorite_color(dictionary: dict[str, str]) -> str:
    """Will return favorite color from the dictionary."""
    counter: dict[str, int] = dict()
    most_popular: str = ""
    high: int = 0
    for color in dictionary.values():
        if color in counter:
            counter[color] += 1
        else:
            counter[color] = 1
        if counter[color] > high:
            most_popular = color
            high = counter[color]
    return most_popular
    

def count(values: list[str]) -> dict[str, int]:
    """Counts the number of unique values in dictionary."""
    dictionary: dict[str, int] = {}
    for value in values:
        if value in dictionary:
            dictionary[value] += 1
        else:
            dictionary[value] = 1
    return dictionary


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Place words in groups based on first letter."""
    dictionary: dict[str, list[str]] = {}
    for word in words:
        key: str = word[0].lower()
        if key in dictionary:
            dictionary[key].append(word)
        else:
            dictionary[key] = [word]
    return dictionary 


def update_attendance(students: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendace."""
    if day == "" or student == "":
        raise 
    else:
        students[day] = [student]
    return students