import turtle

# Const
width = 30
speed = 1
colors = ['#191919', '#333333', '#4d4d4d', '#666666', '#808080', '#999999', '#b3b3b3', '#cccccc', '#e6e6e6']

# Parameters
turtle.shape('turtle')
turtle.shapesize(2)
turtle.speed(speed)


def sq(a):
    """Trajectory for drawing"""
    turtle.begin_fill()
    for k in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()


for i in range(200):
    sq(width)
    turtle.color('#000', colors[i % 9])
    speed = speed + 1
    turtle.speed(speed)
    turtle.right(10)
    width = width + 3

# The end :)
turtle.hideturtle()
input("Press any key to exit...")
