import tkinter as tk
import customtkinter as ctk
from tkinter import *


class LogIn(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        parent.config(width=200,height=200) 
        font_frame = my_font = ctk.CTkFont(size=18)
        title_font_frame = my_font = ctk.CTkFont(size=38)

        label_title = ctk.CTkLabel(self, text="Iniciar Sesion", 
                            font=title_font_frame).place(x=408, y=65)
        
        label1 = Label(self, text="").grid(row=0, column=0,padx=1000,pady=1000)

        # Add the login widgets to this frame
        label_username = ctk.CTkLabel(self, text="Nombre de usuario", 
                            font=font_frame).place(x=440, y=90+78)
        
        self.entry_username = ctk.CTkEntry(self, width=300,
                               height=30,
                               border_width=2, font=font_frame)
        self.entry_username.focus()
        self.entry_username.place(x=365, y=130+78)

        label_password = ctk.CTkLabel(self, text="Contraseña",
                                font=font_frame).place(x=470, y=180+78)
    
        self.entry_password = ctk.CTkEntry(self, show="*", width=300,
                               height=30,
                               border_width=2, font=font_frame)
        self.entry_password.focus()
        self.entry_password.place(x=365, y=220+78)
        
        button_1 = ctk.CTkButton(self, text="Ingresar", font=font_frame, height=40,
                    command=lambda: controller.verification(self.entry_username,self.entry_password)).place(x=446, y=280+78)

    def clean_entries(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)