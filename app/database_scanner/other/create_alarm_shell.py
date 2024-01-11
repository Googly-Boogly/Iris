import tkinter as tk
import pygame

class BooleanToggleApp:
    def __init__(self):
        self.init_sound()  # Initialize pygame.mixer first
        self.boolean_variable = False
        self.create_gui_window()

    def init_sound(self):
        pygame.init()
        self.sound = pygame.mixer.Sound('alarm_sound.wav')  # Replace with your sound file
        self.sound_playing = False

    def toggle_bool(self):
        self.boolean_variable = not self.boolean_variable
        self.update_label()
        if self.boolean_variable:
            self.play_sound()
        else:
            self.stop_sound()

    def update_label(self):
        if self.boolean_variable:
            self.label.config(text="Boolean Variable: True")
        else:
            self.label.config(text="Boolean Variable: False")

    def create_gui_window(self):
        # Create a GUI window
        self.root = tk.Tk()
        self.root.title("Boolean Toggle")

        # Set the window size (width x height) and background color
        window_width = 400
        window_height = 300
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg="black")  # Set the background color to black

        # Create a label to display the boolean variable
        self.label = tk.Label(self.root, text="Boolean Variable: False", fg="white", bg="black")  # Set text color to white
        self.label.pack()

        # Create a button to toggle the boolean variable with a specific size, white border, black background, and white text
        button_width = 100
        button_height = 30
        toggle_button = tk.Button(
            self.root,
            text="Toggle",
            command=self.toggle_bool,
            width=button_width,
            height=button_height,
            highlightthickness=5,  # Set the border thickness to 5 pixels
            highlightbackground="white",  # Set the border color to white
            bg="black",  # Set the background color to black
            fg="white"  # Set the text color to white
        )
        toggle_button.pack()

        # Run the GUI event loop
        self.toggle_bool()
        self.root.mainloop()

    def play_sound(self):
        if not self.sound_playing:
            pygame.mixer.Channel(0).play(self.sound, loops=-1)  # Play the sound continuously
            self.sound_playing = True

    def stop_sound(self):
        pygame.mixer.Channel(0).stop()  # Stop playing the sound
        self.sound_playing = False

# Create an instance of the BooleanToggleApp class to create the GUI window
# app = BooleanToggleApp()
