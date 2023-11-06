"""Combining two lists into a dictionary."""

__author__ = "730478392"


def zip(a: list[str], b: list[int]) -> dict[str, int]:
    """Produce dictionary where both lists are included as keys and values respectively."""
    rdict: dict[str, int] = {}

    if len(a) == 0:
        return rdict
    elif len(a) != len(b):
        return rdict
    
    for i in range(len(a)):
        rdict[a[i]] = b[i]

    return rdict


print(zip(["Laura", "Heidi", "Kayden"], [1, 2, 3]))