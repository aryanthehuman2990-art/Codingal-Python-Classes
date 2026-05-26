import turtle
turtle.Screen().bgcolor("brown")
turtle.color("yellow")
t=turtle.Screen()
t.setup(500,500)
turtle.title("Turtle")
drawing=turtle.Turtle()
for i in range(8):
    drawing.forward(100)
    drawing.right(45)
    i=i+1