"""Intro to object oriented programming."""

from __future__ import annotations 

_author_ = "730478392"


class Point: 
    """Defines a class of 2d Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        """Consturcturs a Point."""
        self.x: float = x_init
        self.y: float = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates existing Point."""
        self.x = self.x * factor
        self.y = self.y * factor 

    def scale(self, factor: int) -> Point:
        """Creates new Point and scales it."""
        return Point(self.x * factor, self.y * factor)