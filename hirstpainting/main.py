import turtle

import colorgram
import random
from turtle import Turtle,Screen
t=Turtle()
turtle.colormode(255)
sc=Screen()
colors=colorgram.extract("image.jpg",84)

# colorlist=[]
# for i in colors:
#    red=i.rgb.r
#    green=i.rgb.g
#    blue=i.rgb.b
#    new=(red,green,blue)
#    colorlist.append(new)
# print(colorlist)
colorlist=[ (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
dot_number=100
t.setheading(230.0)
t.penup()
t.forward(250)
t.setheading(0)
t.speed("fastest")
for i in range(1,101):
    randomcolor = random.choice(colorlist)
    t.dot(20,randomcolor)
    t.penup()
    t.forward(50)
    if i%10==0:
        t.left(90.0)
        t.forward(50)
        t.left(90.0)
        t.forward(500)
        t.setheading(0)
t.hideturtle()
sc.exitonclick()
