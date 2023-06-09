import tkinter as tk
import turtle
from tkinter import filedialog, Label, messagebox, StringVar, Button, OptionMenu, IntVar
import colorgram
from PIL import Image, ImageTk
from dot_art import DotArtMaker
from circle_art import CircleArt
from random_walk_art import RandomWalkArt

# Create the Tkinter window
window = tk.Tk()
window.title("Art Maker")

rgb_colors = []
brightness_threshold = 400  # Adjust this threshold according to your needs
palette_amount = 50
dot_menu = None
circle_menu = None
current_dropdown_menu = None
filepath = ""
size_mapping = {"A4": (1754, 1240), "A3": (2480, 1754), "A2": (3508, 2480)}
circle_count = tk.IntVar()  # Use IntVar to store the number of circles
image_var = tk.StringVar()


#################### Color selection ####################

def choose_image():
    global filepath, rgb_colors
    # Clear the previous palette colors
    rgb_colors = []

    # Open file dialog to select an image file
    filepath = filedialog.askopenfilename(filetypes=[("jpg files", "*.jpg"), ("jpeg files", "*.jpeg")])
    if filepath:
        image_var.set(filepath)
    # Process the selected image path
    if filepath:
        # Process the image file
        print("Selected image:", filepath)
        colors = colorgram.extract(filepath, palette_amount)  # Extract more colors initially

        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b

            # Calculate the brightness of the color
            brightness = (r + g + b) / 3

            if brightness < brightness_threshold and len(rgb_colors) < 100:
                new_colour = (r, g, b)
                if new_colour not in rgb_colors:  # Check for uniqueness
                    rgb_colors.append(new_colour)
            elif len(rgb_colors) >= 100:
                break
        show_image()
    else:
        # Display an error message if no image is chosen or if the path is invalid
        messagebox.showerror("Error", "No image selected or invalid file path. Please try again.")


#################### ART section ####################

def create_art():
    art_type = art_var.get()
    file_path = image_var.get()

    if file_path:
        if art_type == "Dot Art":
            dot_count = dot_var.get()
            dot_art_maker = DotArtMaker(rgb_colors, dot_count)
            dot_art_maker.screen.clear()
            dot_art_maker.create_dot_art()

        elif art_type == "Random Walk Art":
            size = size_var.get()
            canvas_width, canvas_height = size_mapping[size]
            random_walk_art = RandomWalkArt(size, canvas_width, canvas_height)
            random_walk_art.screen.clear()
            random_walk_art.random_walk(1000, rgb_colors)

        elif art_type == "Circle Art":
            circle_count_val = circle_count.get()
            if circle_count_val > 0:
                circle_art = CircleArt()
                circle_art.draw_art(rgb_colors, circle_count_val)

            else:
                messagebox.showerror("Error", "Please select a positive number of circles.")
    else:
        messagebox.showerror("Error", "No image selected or invalid file path. Please try again.")


#################### GUI ####################

def create_dropdown_menu(options, default_value):
    var = tk.StringVar()
    var.set(default_value)  # Set the default value
    menu = tk.OptionMenu(window, var, *options)
    menu.grid(row=0, column=2, padx=10, pady=10)
    return var, menu


# Create a button to choose an image
choose_button = Button(window, text="Choose Image", command=choose_image)
choose_button.grid(row=0, column=0, padx=15, pady=15)

art_options = ["Dot Art", "Random Walk Art", "Circle Art"]
art_var = tk.StringVar(window)
art_var.set(art_options[0])  # Set the default art type
art_menu = OptionMenu(window, art_var, *art_options)
art_menu.grid(row=0, column=1, padx=15, pady=15)

size_var = tk.StringVar()  # Declare size_var as a global variable

create_button = Button(window, text="Create Art", command=create_art)
create_button.grid(row=0, column=3, padx=15, pady=15)


def art_option_selected():
    global current_dropdown_menu, size_var  # Declare size_var as a global variable
    selected_option = art_var.get()

    # Clear the previous dropdown menu
    if current_dropdown_menu is not None:
        current_dropdown_menu[1].destroy()

    # Create a new dropdown menu based on the selected option
    if selected_option == "Dot Art":
        dot_options = [100, 225, 400]
        dot_var, dot_menu = create_dropdown_menu(dot_options, dot_options[0])
        current_dropdown_menu = (dot_var, dot_menu)
    elif selected_option == "Random Walk Art":
        size_options = ["A4", "A3", "A2"]
        size_var, size_menu = create_dropdown_menu(size_options, size_options[0])  # Assign size_var
        current_dropdown_menu = (size_var, size_menu)
    elif selected_option == "Circle Art":
        circle_options = [5, 7, 10]
        circle_count.set(circle_options[0])  # Set the default value for circle_count
        circle_menu = OptionMenu(window, circle_count, *circle_options)
        circle_menu.grid(row=0, column=2, padx=10, pady=10)
        current_dropdown_menu = (circle_count, circle_menu)


# Set the default value for the art type dropdown menu
art_var.set(art_options[0])

# Set the default value for the argument dropdown menu (dot art)
dot_options = ["100", "225", "400"]
dot_var, dot_menu = create_dropdown_menu(dot_options, dot_options[0])
current_dropdown_menu = (dot_var, dot_menu)

art_var.trace("w", lambda *args: art_option_selected())


def show_image():
    global filepath
    if filepath:
        # Open the image using PIL
        image = Image.open(filepath)

        # Update the window to redraw its contents
        window.update()

        # Calculate the new height based on the desired width of 500 pixels while maintaining the aspect ratio
        width, height = image.size
        new_width = 700
        new_height = int(height * new_width / width)

        # Resize the image
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # Create a Tkinter PhotoImage from the resized image
        photo = ImageTk.PhotoImage(resized_image)

        # Create a Tkinter Label to display the image
        if hasattr(window, "image_label"):
            window.image_label.grid_forget()
        image_label = Label(window, image=photo)
        image_label.grid(row=1, column=0, columnspan=5, padx=30, pady=(0, 30))  # Use grid instead of pack

        # Keep a reference to the PhotoImage object to prevent it from being garbage collected
        image_label.image = photo


    else:
        # Clear the previous image label if no image is chosen or if the path is invalid
        if hasattr(window, "image_label"):
            window.image_label.grid_forget()


#################### QUIT ####################

def quit_app():
    window.destroy()


quit_button = Button(window, text="Quit", command=quit_app)
quit_button.grid(row=0, column=4, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
