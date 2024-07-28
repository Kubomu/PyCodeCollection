from turtle import *

"""
Fidget Spinner Game

A simple game where you can spin a fidget spinner using start and stop buttons.

Example:
    Run the code and click on the start button to spin the spinner.
    Click on the stop button to slow it down.

Attributes:
    spinner_radius (int): The radius of the spinner.
    spinner_speed (int): The current speed of the spinner.
    spinner_colors (list): A list of colors for the spinner.
    angle (int): The current angle of the spinner.
"""

speed(0)
bgcolor('lightgray')
title('FIDGET SPINNER GAME')

spinner_radius = 250  # increased radius
spinner_speed = 0
spinner_colors = ['red', 'green', 'blue']
angle = 0

def create_spinner():
    """
    Create the spinner on the screen.

    This function clears the screen, sets up the turtle, and draws the spinner.
    """
    global angle
    clear()
    penup()
    goto(0, 0)  # create the spinner
    setheading(angle)
    pendown()

    for color in spinner_colors:
        fillcolor(color)
        begin_fill()
        circle(spinner_radius / len(spinner_colors))
        end_fill()
        right(360 / len(spinner_colors))

def start_spinner():
    """
    Increase the spinner speed when the start button is clicked.
    """
    global spinner_speed
    spinner_speed += 10
    update_spinner()  # restart the animation

def stop_spinner():
    """
    Decrease the spinner speed when the stop button is clicked.
    """
    global spinner_speed
    spinner_speed = max(0, spinner_speed - 5)

def update_spinner():
    """
    Update the spinner's position and speed.

    This function is called repeatedly to animate the spinner.
    """
    global spinner_speed
    global angle
    if spinner_speed > 0:
        angle += spinner_speed
        angle %= 360  # keep angle within 0-360 range
        spinner_speed -= 1
        create_spinner()
        ontimer(update_spinner, 50)  # continue the animation

def create_buttons():
    """
    Create the start and stop buttons on the screen.
    """
    start_button = Turtle()
    start_button.hideturtle()
    start_button.penup()
    start_button.goto(-100, -200)
    start_button.fillcolor('green')
    start_button.begin_fill()
    start_button.circle(20)
    start_button.end_fill()
    start_button.penup()
    start_button.goto(-100, -220)
    start_button.write("Start", align="center", font=("Arial", 16, "bold"))

    stop_button = Turtle()
    stop_button.hideturtle()
    stop_button.penup()
    stop_button.goto(100, -200)
    stop_button.fillcolor('red')
    stop_button.begin_fill()
    stop_button.circle(20)
    stop_button.end_fill()
    stop_button.penup()
    stop_button.goto(100, -220)
    stop_button.write("Stop", align="center", font=("Arial", 16, "bold"))

    def on_click(x, y):
        if x < -50:  # adjusted click detection
            start_spinner()
        elif x > 50:  # adjusted click detection
            stop_spinner()

    onscreenclick(on_click)

create_spinner()
create_buttons()

mainloop()