import turtle

# Global settings
BACKGROUND_COLOR = "green"  # Background
LINE_COLOR = "blue"  # Color of the Koch snowflake lines
SNOWFLAKE_ORDER = 3  # Order of the Koch snowflake
SNOWFLAKE_SIZE = 200  # Size of the Koch snowflake

def koch_curve(t, order, size):
    """Draw a Koch curve of a given order and size."""
    
    if order == 0:   # The base case is just a straight line.
        t.forward(size)
    else:
        koch_curve(t, order - 1, size / 3) #Go 1/3 of the way.
        t.left(60)
        koch_curve(t, order - 1, size / 3)
        t.right(120)
        koch_curve(t, order - 1, size / 3)
        t.left(60)
        koch_curve(t, order - 1, size / 3)

def draw_snowflake(t, order, size):
    """ Make turtle t draw a Koch fractal of 'order' and 'size'.
        Leave the turtle facing the same direction."""

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Koch Snowflake")

    # Set up the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.color(LINE_COLOR)
    t.hideturtle()

    # Position the turtle and draw the snowflake
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    draw_snowflake(t, SNOWFLAKE_ORDER, SNOWFLAKE_SIZE)

    # Exit on click
    screen.exitonclick()

if __name__ == "__main__":
    main()
