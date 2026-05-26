# 1) Import the `turtle` module:
#    a) This module helps draw shapes and patterns on a screen.
import turtle
# 2) Create the turtle and screen objects:
#    a) Create a turtle pen using `turtle.Turtle()` and store it in a variable.
#    b) Create a screen using `turtle.Screen()` and store it in a variable.
spiral=turtle.Turtle()
screen=turtle.Screen()
# 3) Create a list of colors:
#    a) Store multiple color names in a list (example: red, purple, blue, green, orange, yellow).
list=["violet","indigo","blue","green","yellow","orange","red"]
    # 4) Set up the drawing screen and turtle:
    #    a) Set the background color of the screen to black.
#    b) Set the turtle speed to "fastest" for quick drawing.
#    c) Hide the turtle cursor using `hideturtle()` for a cleaner look.
screen.bgcolor("black")
spiral.speed="fastest"
spiral.hideturtle()
# 5) Start an infinite loop to keep drawing continuously:
#    a) Use `while True:` so the pattern repeats forever.
while True:
    for i in range(200):
        
# 6) Draw the colorful expanding spiral (first loop):
#    a) Use a `for` loop from 0 to 199.
#    b) Change the pen color using the list:
#       - Use `colors[x % len(colors)]` to repeat colors in a cycle.
#    c) Increase the pen width gradually using `width(x/100 + 1)`.
#    d) Move forward by `x` steps to increase the spiral size.
#    e) Turn left by 59 degrees to create the spiral curve.
        spiral.pencolor(list[i % len(list)])
        spiral.width(i/100 + 1)
        spiral.forward(i)
        spiral.left(59)
# 7) Rotate the turtle before drawing the reverse effect:
#    a) Turn right by 239 degrees to shift the direction of the next pattern.
    spiral.right(239) 
# 8) Draw the shrinking “erase” spiral (second loop):
#    a) Use a `for` loop from 200 down to 1.
#    b) Set the pen color to black (same as background) to create an erasing effect.
#    c) Increase pen width (example: `width(x/100 + 7)`) so it covers previous lines.
#    d) Move forward by `x` steps (shrinking movement).
#    e) Turn right by 59 degrees to mirror the spiral effect.
    for x in range(200,0,-1):
        spiral.pencolor("black")
        spiral.width(x/100+7)
        spiral.forward(x)
        spiral.right(59)