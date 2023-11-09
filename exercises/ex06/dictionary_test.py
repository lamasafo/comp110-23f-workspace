"""EX07 Dictionary Testing."""

__author__ = 730478392

from exercises.ex06.dictionary import alphabetizer, invert, count, favorite_color, update_attendance


def test_invert_empty() -> None:
    """Will test that when given an empty dictionary, it returns the same."""
    input: dict[str, str] = {}
    assert invert(input) == {}


def test_invert_one() -> None:
    """Will test that when given a dictionary with one pairing, it returns one inverted pairing."""
    input: dict[str, str] = {'Messi': '10'}
    assert invert(input) == {'10': 'Messi'}


def test_invert_two() -> None:
    """Will test that when given a dictionary with two pairings, it returns the two pairings that are each inverted."""
    input: dict[str, str] = {'Messi': '10', 'Messi': '10'}
    assert invert(input) == {'10': 'Messi', '10': 'Messi'}


def test_count_empty() -> None:
    """Will test that empty dictionary is returned if given an empty list."""
    list_input: list[str] = []
    assert count(list_input) == {}


def test_count_same() -> None:
    """Will test that a dictionary with the count of one value is returned when all the same values are given."""
    list_input: list[str] = ['4', '4', '4', '4', '4', '4', '4', '4']
    assert count(list_input) == {'4': 8}


def test_count_different() -> None:
    """Will test that a dictionary with count of 1 for each value is returned if all items are different."""
    list_input: list[str] = ['yes', 'no']
    assert count(list_input) == {'yes': 1, 'no': 1}


def test_favorite_color_empty() -> None:
    """Will test that when given an empty dictionary, no color is returned."""
    names_and_colors: dict[str, str] = {}
    assert favorite_color(names_and_colors) == ""


def test_favorite_color_tie() -> None:
    """Will test that a tie for favorite color will return the first one inputed."""
    names_and_colors: dict[str, str] = {"Laura": "blue", "Heidi": "black", "Kayden": "gray"}
    assert favorite_color(names_and_colors) == "blue"


def test_favorite_color_frequency() -> None: 
    """Will test that the color with the highest frequency will be returned."""
    names_and_colors: {"Laura": "blue", "Heidi": "black", "Kayden": "gray", "Chichi": "black"}
    assert favorite_color(names_and_colors) == "black"


def test_alphabetizer_empty() -> None:
    """Will test the alphabetizer with an empty list."""
    input_list = []
    assert alphabetizer(input_list) == []


def test_alphabetizer_sorting() -> None:
    """Will test the alphabetizer's ability to put words in alphabetized order."""
    input_list = ["Pizza", "Burger", "Coke"]
    assert alphabetizer(input_list) == ["Pizza", "Burger", "Coke"]


def test_alphabetizer_same() -> None:
    """Will test that if the words have the same initial letter, it'll return them in the order listed."""
    input_list = ["Penguin", "Paper", "Perry"]
    assert alphabetizer(input_list) == ["Penguin", "Paper", "Perry"]


def test_update_attendance_empty() -> None: 
    """Will test an empty attendance dictionary."""
    input_attendance = {}
    result = update_attendance(input_attendance, "Wednesday", "Laura")
    assert result == {}


def test_update_attendance_monday() -> None:
    """Will test today's attendance."""
    input_attendance = {"Wednesday": ["Hanah"]}
    result = update_attendance(input_attendance, "Hanah", "Laura")
    assert result == {"Wednesday": ["Hanah", "Laura"]}


def test_update_attendance_tuesday() -> None:
    """Will test next day's attendance."""
    input_attendance = {"Thursday": ["Hanah"]}
    result = update_attendance(input_attendance, "Friday", "Laura")
    assert result == {"Thursday": ["Hanah"], "Friday": ["Laura"]}