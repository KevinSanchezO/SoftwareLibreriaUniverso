import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the geometry of the main window
        self.geometry("1040x680")

        # Create the container frame
        self.container = tk.Frame(self, bg="#252525")
        self.container.pack(fill="both", expand=True)

        # Create the header frame
        self.header = tk.Frame(self.container, bg="#252525", height=50)
        self.header.grid(row=0, column=0, sticky="ew")

        # Create the logo label
        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 
                                "images")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(self.image_path, 
                                "Logo.png")), size=(276, 48))

        self.logo_frame_label = ctk.CTkLabel(self.header, text="", 
                                image=self.logo_image, compound="left")

        #self.logo = tk.Label(self.header, text="MyApp", font=("Arial", 16), fg="white", bg="#252525")
        self.logo_frame_label.grid(row=0, column=0, padx=10, pady=10)

        # Create the frames
        self.frames = {}
        for F in (Frame1, Frame2):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        # Show the first frame
        self.show_frame(Frame1)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        # Add the login widgets to this frame
        label_username = tk.Label(self, text="Username", 
                        fg="white", bg="#252525").grid(row=0, 
                        column=0, padx=10, pady=10, sticky="w")
        entry_username = tk.Entry(self, bg="white").grid(row=0, 
                        column=1, padx=10, pady=10, sticky="e")
        label_password = tk.Label(self, text="Password", 
                        fg="white", bg="#252525").grid(row=1, 
                        column=0, padx=10, pady=10, sticky="w")
        entry_password = tk.Entry(self, show="*", bg="white").grid(row=1, 
                        column=1, padx=10, pady=10, sticky="e")
        button_1 = tk.Button(self, text="Login", bg="white", fg="#252525", 
                    command=lambda: controller.show_frame(Frame2)).grid(row=2,
                    column=0, columnspan=2, padx=10, pady=10)

class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        # Add the menu buttons to this frame
        button1 = tk.Button(self, text="Option 1", bg="white", fg="#252525")
        button2 = tk.Button(self, text="Option 2", bg="white", fg="#252525")
        button3 = tk.Button(self, text="Option 3", bg="white", fg="#252525")
        button4 = tk.Button(self, text="Option 4", bg="white", fg="#252525")

        # Arrange the buttons in a single row with a padding of 80 pixels
        button1.pack(side="left", padx=80, pady=200)
        button2.pack(side="left", padx=80, pady=200)
        button3.pack(side="left", padx=80, pady=200)
        button4.pack(side="left", padx=80, pady=200)

        # Add a back button to return to the login screen
        back_button = tk.Button(self, text="Back", bg="white", 
                                fg="#252525", 
                                command=lambda: controller.show_frame(Frame1))
        back_button.pack(side="bottom")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()