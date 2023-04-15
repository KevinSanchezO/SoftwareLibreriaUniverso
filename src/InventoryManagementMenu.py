import tkinter as tk
import customtkinter as ctk
from tkinter import *
from PIL import Image,ImageTk

class InventoryManagementMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        font_frame =  ctk.CTkFont(size=18)
        title_font_frame = ctk.CTkFont(size=38)

        label_title = ctk.CTkLabel(self, text="Mantenimiento de inventario", 
                            font=title_font_frame).place(x=30, y=30) 

        #Imagen registrar producto
        global imagenRegistrar
        imgRegistrar = Image.open("images//register.png")
        imgRegistrar = imgRegistrar.resize((100,100),Image.LANCZOS)
        imagenRegistrar = ImageTk.PhotoImage(imgRegistrar)
        lblImagenRegistrar=Label(self,image=imagenRegistrar,bg="#252525").place(x=280,y=190)

        #Imagen Inventario
        global imagenInventario
        imgInventario = Image.open("images//Inventario.png")
        imgInventario = imgInventario.resize((100,100),Image.LANCZOS)
        imagenInventario = ImageTk.PhotoImage(imgInventario)
        lblImagen=Label(self,image=imagenInventario,bg="#252525").place(x=640,y=190)


        # Add the menu buttons to this frame
        button1 = ctk.CTkButton(self, text="Registrar nuevo\nproducto", 
                            font=font_frame,
                            command=lambda: controller.show_frame("RegisterNewProduct"))

        button2 = ctk.CTkButton(self, text="Ver inventario", 
                            font=font_frame,
                            command=lambda: controller.show_frame("ModifyInventory"))

        # Arrange the buttons in a single row with a padding of 80 pixels
        button1.place(x=260,y=300)
        button2.place(x=620,y=315)

        back_button = ctk.CTkButton(self, 
                                    text="Salir", 
                                    font=font_frame,
                                    fg_color="#D61C1C",
                                    hover_color="#9E1818",
                                    command=lambda: controller.show_frame("MainMenu"))
        back_button.place(x=450,y=400)
        

    def clean_entries(self):
        pass