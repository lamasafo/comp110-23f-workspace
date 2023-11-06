"""Test my zip function."""

__author__ = "730478392"

from lessons.zip import zip


def test_length_zero_zip() -> None:
    """Testing dict of length of zero."""
    assert zip([]) == 0


def test_zip_length_two() -> None:
    """Testing lists of length two."""
    assert zip(["Laura", "Heidi"], [1, 2]) == {"Laura": 1, "Heidi": 2}


def test_zip_pos_and_neg() -> None:
    """Testing lists of ppositive and negative values."""
    word_list: list[str] = ["play", "soccer", "food", "pain"]
    number_list: list[int] = [1, 3, -5, -9]
    assert zip(word_list, number_list) == {"play": 1, "soccer": 3, "food": -5, "pain": -9}

