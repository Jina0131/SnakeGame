import re
from turtle import Screen, Turtle
import time
import random as rd

def creat_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orangered")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body)

def up():
    if snakes[0].heading() != 270:
        snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)

def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

def rand_pos():
    rand_x = rd.randint(-250, 250)
    rand_y = rd.randint(-250,250)
    return rand_x, rand_y




screen = Screen()
screen.setup(600, 600)
screen.bgcolor("khaki")
screen.title("Snake Game")
screen.tracer(0)

start_pos = [(0,0), (-20, 0), (-40, 0)]
snakes = []
score = 0
for pos in start_pos:
    creat_snake(pos)


food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.write(f"점수: {score}", font=("", 15, "bold"))

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snakes)-1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())
    snakes[0].forward(10)

    if snakes[0].distance(food) < 15:
        food.goto(rand_pos())
        creat_snake(snakes[-1].pos())