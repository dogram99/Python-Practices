import turtle

# Parameters
turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('green', 'yellow')
turtle.speed(5)


def david():
    """Trajectory for drawing"""
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(60)
            turtle.left(360 / 3)
        turtle.end_fill()

        turtle.forward(60)
        turtle.right(60)


if __name__ == '__main__':
    # Script
    david()
    turtle.backward(200)
    david()
    turtle.hideturtle()

    # The end :)
    input("Press any key to exit...")
