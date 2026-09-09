import turtle
import time
import random

def get_high_score():
    try:
        with open("data.txt", mode="r") as file:
            return int(file.read())
    except FileNotFoundError:
        with open("data.txt", mode="w") as file:
            file.write("0")
        return 0

def update_high_score(new_score):
    with open("data.txt", mode="w") as file:
        file.write(str(new_score))

screen = turtle.Screen()
screen.title("Day 24: Snake Game with High Score Persistence")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

score = 0
high_score = get_high_score()
segments = []

head = turtle.Turtle("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("white")
pen.goto(0, 260)

def update_scoreboard():
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

update_scoreboard()

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

def reset_game():
    global score, high_score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    if score > high_score:
        high_score = score
        update_high_score(high_score)

    score = 0
    update_scoreboard()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

while True:
    screen.update()

    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        reset_game()

    if head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        new_segment = turtle.Turtle("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score
            update_high_score(high_score)
        update_scoreboard()

    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 10:
            reset_game()

    time.sleep(0.1)
