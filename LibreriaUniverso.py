import customtkinter as ctk
import os
from PIL import Image

root = ctk.CTk()

root.title("Libreria Universo")
root.geometry("1040x680")
root.resizable(False, False)
root._set_appearance_mode("dark")

frame_header = ctk.CTkFrame(master = root, width=1040, height=80).place(x=0, y=0)
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Logo.png")), size=(276, 48))

logo_frame_label = ctk.CTkLabel(frame_header, text="", image=logo_image, compound="left")
logo_frame_label.grid(row=0, column=0, padx=20, pady=10)




root.mainloop()
