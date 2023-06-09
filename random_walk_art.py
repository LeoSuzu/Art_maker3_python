import turtle as t
import random

DIRECTIONS = [0, 90, 180, 270]
WALK_DISTANCE = 50

class RandomWalkArt:
    def __init__(self, size, canvas_width, canvas_height):
        self.size = size
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.screen = t.Screen()
        self.screen.title('Random Walk Art Maker')
        self.turtles = self.create_multiple_turtles()

        self.reset_screen()

    def create_multiple_turtles(self):
        turtles = []
        num_turtles = 30

        for _ in range(num_turtles):
            turtle = t.Turtle()
            turtle.hideturtle()
            turtle.penup()
            turtle.pensize(10)
            turtle.speed("fastest")
            turtles.append(turtle)

        for turtle in turtles:
            turtle.goto(0, 0)

        return turtles

    def reset_screen(self):
        # Clear the screen and set up the canvas
        self.screen.clear()
        self.screen.setup(self.canvas_width, self.canvas_height)

    def random_walk(self, num_steps, rgb_colors):
        self.reset_screen()
        self.screen.tracer(0)

        # Pen down for all turtles
        for turtle in self.turtles:
            turtle.pendown()

        t.colormode(255)

        for _ in range(num_steps):
            for turtle in self.turtles:
                turning = random.choice(DIRECTIONS)
                turtle.setheading(turning)
                turtle.forward(WALK_DISTANCE)

                if (
                        turtle.xcor() >= 1450
                        or turtle.xcor() <= -1450
                        or turtle.ycor() >= 700
                        or turtle.ycor() <= -700
                ):
                    # If turtle reaches the screen boundary, make it move inwards and reset its position
                    turtle.right(90)
                    turtle.forward(WALK_DISTANCE)
                    turtle.right(90)
                    turtle.forward(WALK_DISTANCE)
                    turtle.penup()
                    turtle.home()
                    turtle.pendown()
                else:
                    # Choose a random color from the provided palette and set the pen color
                    color = random.choice(rgb_colors)
                    r, g, b = color
                    turtle.pencolor(r, g, b)

            self.screen.update()

        self.screen.update()
        self.screen.exitonclick()
