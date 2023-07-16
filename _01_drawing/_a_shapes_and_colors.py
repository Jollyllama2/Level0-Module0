import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    my_dog = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    my_dog.shape("turtle")
    # Set your turtle's speed using .speed(2)
    my_dog.speed(9)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    my_dog.color('red')
    my_dog.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range(4):
        my_dog.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        my_dog.left(90)
        my_dog.forward(100)
        my_dog.right(90)
        my_dog.forward(100)
        my_dog.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    my_dog.penup()
    # Move your turtle to a new place on the screen using .goto(x, y)
    my_dog.goto(x=23, y=13)
    # x=0 and y=0 is the center of the screen
    my_dog.begin_fill()
    # Have your turtle draw a circle using .circle(radius, steps=30)
    my_dog.circle(60, steps=30)

   # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    my_dog.end_fill()
    # Draw 3 more shapes with different fill colors!
    my_dog.goto(x=-50, y=-40)
    my_dog.pendown()
    for i in range(4):
        my_dog.left(90)
        my_dog.forward(100)
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
