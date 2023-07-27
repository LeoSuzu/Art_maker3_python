from turtle import Turtle, Screen
import random

class CircleArt:
    def __init__(self):
        # Canvas settings and screen size 720dpi
        self.screen = Screen()
        self.screen.setup(2560, 1600)
        self.screen.screensize(1080, 720)
        self.screen.colormode(255)

        # Turtle module settings
        self.turtle = Turtle()
        self.turtle.speed("fastest")
        self.turtle.hideturtle()
        self.turtle.pensize(50)

    def position(self):
        """
        Generates a random position within a certain range.
        Returns:
            tuple: x, y coordinates of the position.
        """
        position_x = random.randint(-600, 600)
        position_y = random.randint(-400, 400)
        new_position = (position_x, position_y)
        return new_position

    def draw_art(self, rgb_colors, circle_count):
        """
        Draws the circle art.
        Args:
            rgb_colors (list): List of RGB colors.
            circle_count (int): Number of circles to draw.
        """
        for i in range(int(circle_count)):
            self.turtle.speed("fastest")
            self.turtle.hideturtle()
            for _ in range(int(360 / 80)):
                color = random.choice(rgb_colors)
                self.turtle.penup()
                self.turtle.forward(random.randint(50, 150))
                self.turtle.pencolor(color)
                self.turtle.pendown()
                self.turtle.circle(1200)
                self.turtle.setheading(self.turtle.heading() - 80)
            self.turtle.penup()
            self.turtle.setpos(self.position())
            self.turtle.pendown()

        self.screen.exitonclick()
