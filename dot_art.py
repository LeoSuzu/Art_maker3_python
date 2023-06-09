import turtle as t
import random


class DotArtMaker:
    def __init__(self, rgb_colors, dot_count):
        self.rgb_colors = rgb_colors
        self.dot_count = int(dot_count)
        self.t = t
        self.screen = self.t.Screen()
        self.screen.title("Dot Art Maker")

    def create_dot_art(self):
        global canvas_width, canvas_height
        self.screen.clear()  # Clear the screen before creating new art
        self.t.clear()
        self.t.penup()
        self.t.hideturtle()

        dot_count = self.dot_count

        # Starting position set
        if dot_count == 100:
            self.t.setpos(-230, -220)
        elif dot_count == 225:
            self.t.setpos(-375, -340)
        elif dot_count == 400:
            self.t.setpos(-470, -470)

        # Adjust canvas size based on dot count
        if dot_count == 100:
            canvas_width = 805
            canvas_height = 800
        elif dot_count == 225:
            canvas_width = 1200
            canvas_height = 1200
        elif dot_count == 400:
            canvas_width = 1500
            canvas_height = 1500

        self.screen.setup(canvas_width, canvas_height)
        t.colormode(255)  # Set the color mode to 255

        for i in range(dot_count):
            color = random.choice(self.rgb_colors)  # Use the extracted colors
            r, g, b = color  # Extract RGB values from the tuple
            self.t.dot(30, (r, g, b))  # Pass the RGB tuple directly to t.dot()

            if dot_count == 100:
                self.t.forward(50)
                if (i + 1) % 10 == 0:
                    self.t.setheading(90)
                    self.t.forward(50)
                    self.t.setheading(180)
                    self.t.forward(550)
                    self.t.setheading(0)
                    self.t.forward(50)  # Additional forward step for the next row

            elif dot_count == 225:
                self.t.forward(50)
                if (i + 1) % 15 == 0:
                    self.t.setheading(90)
                    self.t.forward(50)
                    self.t.setheading(180)
                    self.t.forward(800)
                    self.t.setheading(0)
                    self.t.forward(50)  # Additional forward step for the next row

            elif dot_count == 400:
                self.t.forward(50)
                if (i + 1) % 20 == 0:
                    self.t.setheading(90)
                    self.t.forward(50)
                    self.t.setheading(180)
                    self.t.forward(1050)
                    self.t.setheading(0)
                    self.t.forward(50)  # Additional forward step for the next row

        self.screen.exitonclick()

    def clear_screen_dot(self):
        self.screen.clear()
