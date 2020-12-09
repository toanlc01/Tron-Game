import turtle

button = turtle.Turtle()
button.color('black')
button.hideturtle()
for i in range(2):
        button.forward(80)
        button.left(90)
        button.forward(30)
        button.left(90)
button.penup()
button.goto(20,5)
button.write('Start!',font=('Arial',12,'normal'))
# create a screen
def click(x,y):
        if x > 0 and x < 81 and y > 0 and y < 30:
                        

                screen = turtle.Screen()
                screen.setup(1800, 1200, 0, 0)
                screen.bgcolor('black')

                # Making border

                border = turtle.Turtle()
                border.penup()
                border.setposition(-700, 400)
                border.pendown()
                border.pensize(10)
                border.color('pink')
                border.speed(0)
                for loop in range(2):
                        border.forward(1400)
                        border.right(90)
                        border.forward(800)
                        border.right(90)
                border.hideturtle()

                # set up key to control 1st turtle

                def turnup1():
                        global speed1
                        speed1 = 5
                        if int(turtle1.heading()) in [0, 180]:
                                turtle1.setheading(90)
                def turndown1():
                        global speed1
                        speed1 = 5
                        if int(turtle1.heading()) in [0, 180]:
                                turtle1.setheading(270)
                def turnleft1():
                        global speed1
                        speed1 = 5
                        if int(turtle1.heading()) in [90, 270]:
                                turtle1.setheading(180)
                def turnright1():
                        global speed1
                        speed1 = 5
                        if int(turtle1.heading()) in [90, 270]:
                                turtle1.setheading(0)

                def increasespeed_upkey1():
                        global speed1
                        if int(turtle1.heading()) == 90:
                                speed1 += 5
                def increasespeed_downkey1():
                        global speed1
                        if int(turtle1.heading()) == 270:
                                speed1 += 5
                def increasespeed_leftkey1():
                        global speed1
                        if int(turtle1.heading()) == 180:
                                speed1 += 5
                def increasespeed_rightkey1():
                        global speed1
                        if int(turtle1.heading()) == 0:
                                speed1 += 5
                turtle.onkey(turnup1, "Up")
                turtle.onkey(turndown1, "Down")
                turtle.onkey(turnleft1, "Left")
                turtle.onkey(turnright1, "Right")
                turtle.onkeypress(increasespeed_upkey1,"Up")
                turtle.onkeypress(increasespeed_downkey1,"Down")
                turtle.onkeypress(increasespeed_leftkey1,"Left")
                turtle.onkeypress(increasespeed_rightkey1,"Right")
                turtle.listen()

                # create the first turtle and set the starting position

                turtle1 = turtle.Turtle()
                turtle1.hideturtle()
                turtle1.penup()
                turtle1.setposition(100,0)
                turtle1.setheading(90)
                turtle1.showturtle()
                turtle1.pendown()
                turtle1.color('lightblue')
                turtle1.shape('turtle')
                turtle1.speed(0)
                speed1 = 5


                # set up the control for 2nd turtle

                def turnup2():
                        global speed2 
                        speed2 = 5
                        if int(turtle2.heading()) in [0, 180]:
                                turtle2.setheading(90)
                def turndown2():
                        global speed2 
                        speed2 = 5
                        if int(turtle2.heading()) in [0, 180]:
                                turtle2.setheading(270)
                def turnleft2():
                        global speed2 
                        speed2 = 5
                        if int(turtle2.heading()) in [90, 270]:
                                turtle2.setheading(180)
                def turnright2():
                        global speed2 
                        speed2 = 5
                        if int(turtle2.heading()) in [90, 270]:
                                turtle2.setheading(0)

                def increasespeed_upkey2():
                        global speed2
                        if int(turtle2.heading()) == 90:
                                speed2 += 5
                def increasespeed_downkey2():
                        global speed2
                        if int(turtle2.heading()) == 270:
                                speed2 += 5
                def increasespeed_leftkey2():
                        global speed2
                        if int(turtle2.heading()) == 180:
                                speed2 += 5
                def increasespeed_rightkey2():
                        global speed2
                        if int(turtle2.heading()) == 0:
                                speed2 += 5

                turtle.onkey(turnup2, "w")
                turtle.onkey(turndown2, "s")
                turtle.onkey(turnleft2, "a")
                turtle.onkey(turnright2, "d")
                turtle.onkeypress(increasespeed_upkey2,"w")
                turtle.onkeypress(increasespeed_downkey2,"s")
                turtle.onkeypress(increasespeed_leftkey2,"a")
                turtle.onkeypress(increasespeed_rightkey2,"d")

                # create the second turtle and set the starting position

                turtle2 = turtle.Turtle()
                turtle2.hideturtle()
                turtle2.penup()
                turtle2.setposition(-100,0)
                turtle2.setheading(90)
                turtle2.showturtle()
                turtle2.pendown()
                turtle2.color('orange')
                turtle2.shape('turtle')
                turtle2.speed(0)
                speed2 = 5

                # Running the 2 turtles

                turtle1_coord = []
                turtle2_coord = []

                while  True:
                        turtle1.forward(speed1)
                        turtle1_coord.append([int(turtle1.xcor()), int(turtle1.ycor())])
                        turtle2.forward(speed2)
                        turtle2_coord.append([int(turtle2.xcor()), int(turtle2.ycor())])
                        if turtle1_coord.count([int(turtle1.xcor()), int(turtle1.ycor())]) != 1:
                                turtle.color('orange')
                                style = ('Courier', 30, 'bold')
                                turtle.write('Player 1 Wins!', font=style, align='center')
                                turtle.hideturtle()
                                break
                        elif turtle2_coord.count([int(turtle2.xcor()), int(turtle2.ycor())]) != 1:
                                turtle.color('Light Blue')
                                style = ('Courier', 30, 'bold')
                                turtle.write('Player 2 Wins!', font=style, align='center')
                                turtle.hideturtle()
                                break
                        elif [int(turtle1.xcor()), int(turtle1.ycor())] in turtle2_coord:
                                turtle.color('orange')
                                style = ('Courier', 30, 'bold')
                                turtle.write('Player 1 Wins!', font=style, align='center')
                                turtle.hideturtle()
                                break
                        elif [int(turtle2.xcor()), int(turtle2.ycor())] in turtle1_coord:
                                turtle.color('Light Blue')
                                style = ('Courier', 30, 'bold')
                                turtle.write('Player 2 Wins!', font=style, align='center')
                                turtle.hideturtle()
                                break
                        elif int(turtle1.xcor()) not in range(-700, 700) or int(turtle1.ycor()) not in range(-400, 400):
                                turtle.color('orange')
                                style = ('Courier', 30, 'bold')
                                turtle.write('Player 1 Wins!', font=style, align='center')
                                turtle.hideturtle()
                                break 
                        elif int(turtle2.xcor()) not in range(-700, 700) or int(turtle2.ycor()) not in range(-400, 400):
                                turtle.color('Light Blue')
                                style = ('Courier', 30, 'bold')
                                turtle.write('Player 2 Wins!', font=style, align='center')
                                turtle.hideturtle()
                                break
                        if turtle1.ycor() not in range(-400, 400):
                            turtle.color('orange')
                            style = ('Courier', 30, 'bold')
                            turtle.write('Player 1 Wins!', font=style, align='center')
                            turtle.hideturtle()
                            break 
                        if turtle2.ycor() not in range(-400, 400):
                            turtle.color('Light Blue')
                            style = ('Courier', 30, 'bold')
                            turtle.write('Player 2 Wins!', font=style, align='center')
                            turtle.hideturtle()
                            break
                screen.mainloop()
turtle.onscreenclick(click,1)
turtle.listen()
turtle.done()