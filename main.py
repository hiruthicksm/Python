import random

from turtle import Turtle,Screen
sc=Screen()
sc.setup(height=450,width=600)

bet=sc.textinput(title="Place the bet",prompt="Enter which turtle will win the race?")

y_pos=[-150,-100,-50,0,50,100,150]
color_list=["violet","indigo","blue","green","yellow","orange","red"]
speed_list=[5,10,2,4,3,1,5]
turlist=[]
flag=True
for i in range(0,7):
    tim =Turtle(shape="turtle")
    tim.color(color_list[i])
    tim.penup()
    tim.goto(x=-285,y=y_pos[i])

    turlist.append(tim)
while flag:
    for i in turlist:
        
        i.forward(random.randint(0,10))
        if i.xcor()>270:
            flag=False
            win_color=i.pencolor()
            if win_color==bet:
                print("You have won the bet")
            else:
                print(f"Sorry {win_color} is the Winner, you lose")
sc.exitonclick()


