from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def turn_left():
    tim.setheading(tim.heading() + 20)


def turn_right():
    tim.right(20)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(screen.resetscreen, "c")
screen.exitonclick()
