from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500 , height=400)
user_guess = screen.textinput(title="Bet",prompt="which turtle win race? Enter a color : ")
colors = ["red","orange","yellow","blue","green","purple"]
y_postions = [-70,-40,-10,20,50,80]
all_turtles = []
is_race_on = False
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=y_postions[i])
    all_turtles.append(tim)
if user_guess:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won !! The {winning_color} is winner")
            else:
                print(f"You've lost !! The {winning_color} is winner")
            break
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)

screen.exitonclick()