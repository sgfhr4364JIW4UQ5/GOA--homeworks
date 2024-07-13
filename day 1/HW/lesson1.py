from turtle import*
#we awnt to paint a house

#STEP 1: draw a square

speed(30)
width("5")
color("blue")
begin_fill


forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()

#end of square


#drawing a door

begin_fill()

forward(70)
color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()



penup
goto(200,200)
pendown

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup
goto(150,150)
pendown
 
color("cyan")
begin_fill()

left(30)
forward(50)
left(90)
forward(35)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

penup
goto(10,100)
pendown

begin_fill()

right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()





exitonclick()