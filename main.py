import turtle
from random import randint
import time

turtle_board = turtle.Screen()
turtle_board.bgcolor("Light blue")
turtle_board.title("python game turtle")

turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("green")
turtle_instance.shapesize(1.5)
turtle_instance.settiltangle(90)
turtle_instance.up()

score_text = turtle.Turtle()
score_text.up()
score_text.hideturtle()
score_text.left(90)
score_text.forward(150)
score_text.left(90)
score_text.forward(50)
score = 0

times = 15
time_text = turtle.Turtle()
time_text.up()
time_text.hideturtle()
time_text.left(90)
time_text.forward(180)
time_text.left(90)
time_text.forward(50)


def show_score():
    score_text.clear()
    score_text.write(f"score: {score}", font=("monospace", 16))

def add_score(x, y):
    global score
    score += 1
    show_score()


def show_time ():
    time_text.clear()
    time_text.write(f"time: {times}", font=("monospace", 16))


def change_time ():
    while True:
        turtle_jump()
        time.sleep(1)
        global times
        times = times -1
        show_time()
        if times == 0:
            time_text.clear()
            time_text.write("game over!", font=("monospace", 16))
            time.sleep(5)
            turtle_board.bye()

def turtle_jump ():
    if 1 == 1:
        turtle_instance.speed(0)
        turtle_instance.hideturtle()
        turtle_instance.setheading(turtle_instance.heading() - 60)
        turtle_instance.setpos(randint(-250, 250), randint(-250, 250))
        turtle_instance.showturtle()

turtle_instance.onclick(add_score)
show_score()
show_time()
change_time()

turtle.mainloop()
