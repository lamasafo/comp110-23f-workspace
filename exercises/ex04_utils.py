"""EX04 - Creating and Establishing Various Lists."""

__author__ = "730478392"


def all(number_list: list[int], int_input: int) -> bool:
    """"Finding if all numbers in list match the the input."""
    index: int = 0
    while index < len(number_list):
        if number_list[index] != int_input:
            return False
        index += 1
    if len(number_list) == 0:
        return False
    else:
        return True 
    

def max(input: list[int]) -> int:
    """Finding the maximum number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    index: int = 0 
    outcome: int = input[0]
    while index < len(input):
        if outcome < input[index]:
            outcome = input[index]
        index += 1
    return outcome


def is_equal(int_1: list[int], int_2: list[int]) -> bool:
    """Finding if all numbers in two separate lists match each other."""        
    index: int = 0
    if len(int_1) != len(int_2):
        return False
    while index < len(int_1):
        if int_1[index] != int_2[index]:
            return False
        index += 1
    return True
    