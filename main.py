import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 500)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color")
x = -240
y = -100
turtles = []
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    new_turtle.goto(x, y)
    y += 50
    turtles.append(new_turtle)

race_is_on = True
while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230 :
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You WON, the {winning_turtle} turtle WON")
            else:
                print(f"You LOST, the {winning_turtle} turtle WOM")
        else:
            distance = random.randint(0,10)
            turtle.forward(distance)





screen.exitonclick()