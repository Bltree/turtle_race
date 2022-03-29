import turtle
from turtle import Turtle, Screen
import random

is_rance_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = 150

all_wangba = []

for color in colors:
    wangba = Turtle()
    wangba.shape("turtle")
    wangba.color(color)
    wangba.penup()
    wangba.goto(-230, y)
    y -= 60
    all_wangba.append(wangba)

if user_bet:
    is_rance_on = True

while is_rance_on:
    for wugui in all_wangba:
        if wugui.xcor() > 230:
            is_rance_on = False
            winning_turtle = wugui.pencolor()
            if winning_turtle == user_bet:
                print(f"You've win! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        turtle_pace = random.randint(0, 10)
        wugui.forward(turtle_pace)


screen.exitonclick()
