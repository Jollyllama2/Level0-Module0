import random
import turtle


# Returns a random color!
def get_random_color():
    return  (random.randint(0, 255))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    window.colormode(255)
    # Make a new turtle
    my_shark = turtle.Turtle()
    # This code sets our shape to a turtle
    my_shark.shape('turtle')
    # Set your turtle's speed (0=fastest, 1=slowest, 10=faster)
    my_shark.speed(10)
    # Set your turtle's color using .color('green')
    my_shark.color('green')

    # Use a loop to repeat a the code below 50 times
    for i in range(50):
        print(get_random_color())
     # Set the turtle color to a random color
        my_shark.color(get_random_color(),get_random_color(),get_random_color())
        # Move the turtle (5*i) pixels. 'i' is the loop variable
        my_shark.forward(5*i)
        # Turn the turtle (360/7) degrees to the right
        my_shark.right(360/7)
        # Change the turtle width to 'i' (the loop variable)
        my_shark.width(i)
        # Check the pattern against the picture in the recipe. If it matches, you are done!

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
