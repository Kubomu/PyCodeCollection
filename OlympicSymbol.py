# OlympicSymbol.py
import turtle

def draw_olympic_symbol():
    """
    Draws the Olympic symbol using turtle graphics.

    The Olympic symbol consists of five interconnected rings of equal size,
    colored blue, yellow, black, green, and red, respectively.

    Example:
        >>> draw_olympic_symbol()
        # This will draw the Olympic symbol on the screen

    Returns:
        None
    """
    turtle.title("OLYMPIC SYMBOL")
    turtle.bgcolor("grey")

    turtle.color("blue")   # blue circle
    turtle.penup()
    turtle.goto(-110, -25)
    turtle.pendown()
    turtle.circle(45)

    turtle.color("black")
    turtle.penup()
    turtle.goto(0, -25)
    turtle.pendown()
    turtle.circle(45)      # black circle

    turtle.color("red")
    turtle.penup()
    turtle.goto(110, -25)
    turtle.pendown()
    turtle.circle(45)       # red circle

    turtle.color("yellow")
    turtle.penup()
    turtle.goto(-55, -75)
    turtle.pendown()
    turtle.circle(45)      # yellow circle 

    turtle.color("green")
    turtle.penup()
    turtle.goto(55, -75)
    turtle.pendown()
    turtle.circle(45)      # green circle

    turtle.done()      # pause

if __name__ == "__main__":
    draw_olympic_symbol()