"""Summing the elements of a list using different loops."""

__author__ = "730478392"


def w_sum(vals: list[float]) -> float: 
    """Summing elements using while loop."""
    current_sum: float = 0.0
    idx: int = 0
    while idx < len(vals): 
        current_sum += vals[idx]
        idx += 1
    return current_sum 


def f_sum(vals: list[float]) -> float:
    """Summing elements using for loop."""
    current_sum = 0.0
    for value in vals:
        current_sum += value
    return current_sum
    

def f_range_sum(vals: list[float]) -> float:
    """Summing elements using for loop and range."""
    current_sum = 0.0
    for idx in range(len(vals)):
        print(idx)
        current_sum += vals[idx]
        print(current_sum)
    return current_sum 