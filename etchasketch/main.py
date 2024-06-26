from turtle import Turtle,Screen
tim=Turtle()
sc=Screen()
sc.listen()
def front():
    tim.forward(30)
def back():
    tim.backward(30)
def left():
    tim.left(10.0)

def right():
    tim.right(10.0)

def clear():
    tim.clear()
    tim.reset()
sc.onkey(key="w",fun=front)
sc.onkey(key="s",fun=back)
sc.onkey(key="a",fun=left)
sc.onkey(key="d",fun=right)
sc.onkey(key="c",fun=clear)
sc.exitonclick()