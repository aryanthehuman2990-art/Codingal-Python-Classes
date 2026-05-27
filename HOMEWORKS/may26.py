import turtle
shapes=turtle.Turtle()
screen=turtle.Screen()
shapes.speed="fastest"
bgcolor=["black"]
shapes.hideturtle()
for i in range(10):
    shapes.pendown()
    shapes.pencolor("blue")
    shapes.width(8)
    shapes.forward(50)
    shapes.left(36)
shapes.penup()
shapes.forward(200)
shapes.left(90)
shapes.forward(200)
shapes.pendown()

for x in range(360):
    shapes.pencolor("red")
    shapes.width(5)
    shapes.forward(2)
    shapes.left(1)