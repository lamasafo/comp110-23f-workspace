"""EX05 - Turtle Scene."""

__author__ = "730478392"

from turtle import Turtle, done


def starting_position(turtle: Turtle, x: float, y: float, rotation: float) -> None:
    """Reset cursor position to draw."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(rotation)


def draw_rectangle(turtle: Turtle, x: float, y: float, width: float, height: float, rotation: float) -> None:
    """Draw rectangle."""
    starting_position(turtle, x, y, rotation)
    i: int = 0
    while i < 4: 
        if i % 2 == 0:
            turtle.forward(width)
        else: 
            turtle.forward(height)
        i = i + 1 
        turtle.right(90)


def draw_eq_triangle(turtle: Turtle, x: float, y: float, side: float, rotation: float) -> None:
    """Draw equilateral triangle."""
    starting_position(turtle, x, y, rotation)
    i: int = 0
    while i < 3: 
        turtle.forward(side)
        i = i + 1
        turtle.right(120)


def draw_hexagon(turtle: Turtle, x: float, y: float, side_length: float, rotation: float) -> None: 
    """Draw a hexagon."""
    starting_position(turtle, x, y, rotation)
    i: int = 0
    while i < 6:
        turtle.forward(side_length)
        i = i + 1
        turtle.right(60)


def draw_star(turtle: Turtle, x: float, y: float, range: int, rotation: float) -> None:
    """Draw a star."""
    starting_position(turtle, x, y, rotation)
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)


def main() -> None:
    """Starting point of scene."""
    leo: Turtle = Turtle()
    draw_star(leo, 5, 300, 5, 38)
    leo.begin_fill
    draw_star(leo, -5, -80, 5, -38)
    leo.end_fill
    draw_rectangle(leo, -100, 130, 40, 60, 0)
    draw_eq_triangle(leo, 40, 180, 12, 0)
    leo.pencolor("green")
    leo.begin_fill
    draw_hexagon(leo, -80, -120, 8, 0)
    leo.color("red")
    leo.end_fill
    done()
    if __name__ == "_main_": 
        main()