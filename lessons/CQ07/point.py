"""Creating a class point."""

from __future__ import annotations 

_author_ = "730478392"


class Point: 
    """Class represents a Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Constructs a Point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scale a point by a certain factor."""
        self.x = self.x * factor
        self.y = self.y * factor 

    def scale(self, factor: int) -> Point:
        """Creates new Point and scales it."""
        new_x: float = self.x * factor
        new_y: float = self.y * factor 
        new_point: Point = Point(new_x, new_y)
        return new_point 
    
    def __str__(self) -> str:
        """Magic method to print out points as strings."""
        point_place: str = f"x: {self.x}; y: {self.y}"
        return point_place
    
    def __mul__(self, factor: int | float) -> Point:
        """Magic method to multiply a point by a factor."""
        new_x: float = self.x * factor 
        new_y: float = self.y * factor 
        new_point: Point = Point(new_x, new_y)
        return new_point 
    
    def __add__(self, factor: int | float) -> Point:
        """Magic method to to increase a point by x and y attributes."""
        new_x: float = self.x + factor 
        new_y: float = self.y + factor 
        new_point: Point = Point(new_x, new_y)
        return new_point 