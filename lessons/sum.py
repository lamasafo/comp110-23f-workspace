"""Summing the elements of a list using different loops."""

__author__ = "730478392"

"""Summing elements using while loop."""
def w_sum(vals: list[float]) -> float: 
    current_sum: float = 0.0
    idx: int = 0
    while idx < len(vals): 
        current_sum += vals[idx]
        idx += 1
    return current_sum 



"""Summing elements using for loop."""
def f_sum(vals: list[float]) -> float:
    current_sum = 0.0
    for value in vals:
        current_sum += value
    return current_sum
    


"""Summing elements using for loop and range."""
def f_range_sum(vals: list[float]) -> float:
    current_sum = 0.0
    for idx in range(len(vals)):
        current_sum += vals[idx]
        return current_sum