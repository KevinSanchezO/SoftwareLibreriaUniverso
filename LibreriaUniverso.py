import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox
import os
import ConexionBD as bd
import string
import random
import tkinter.font as font
from tkinter import *
from PIL import Image,ImageTk

from src.LogIn import LogIn
from src.MainMenu import MainMenu
from src.InventoryManagementMenu import InventoryManagementMenu
from src.RegisterNewProduct import RegisterNewProduct
from src.RegistrarVenta import RegistrarVenta
from src.ModifyInventory import ModifyInventory

# Supported modes : Light, Dark, System
ctk.set_appearance_mode("System")
 
# Supported themes : green, dark-blue, blue
ctk.set_default_color_theme("blue")   

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the geometry of the main window
        self.geometry("1040x680")

        self.title("Libreria Universo")

        # Create the container frame
        self.container = tk.Frame(self, bg="#252525")
        self.container.pack(fill="both", expand=True)

        # Create the header frame
        self.header = tk.Frame(self.container, bg="#181818", height=50)
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
        self.frames = {
            "LogIn": LogIn,
            "MainMenu": MainMenu,
            "InventoryManagementMenu": InventoryManagementMenu,
            "RegisterNewProduct": RegisterNewProduct,
            "RegistrarVenta": RegistrarVenta,
            "ModifyInventory": ModifyInventory
        }
        
        for name, F in self.frames.items():
            frame = F(self.container, self)
            self.frames[name] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        # Show the first frame
        self.show_frame("RegistrarVenta")

    def verificationRegisterProduct(self,name,date,marca,quantity,price):
        if name.get() == "" or date.get()=="" or marca.get()=="" or quantity.get()=="" or price.get()=="":
            MessageBox.showinfo("Error!", "Por favor ingrese los datos que se le solicitan")
        else:
            coneccion = bd.connect()
            bandera = bd.consultaRegistrarProducto(coneccion,name.get(),date.get(),marca.get(),quantity.get(),price.get())
            MessageBox.showinfo("Aviso!", "Producto ingresado correctamente")
            

    def verification(self,user,password):

        if user.get() == "" or password.get()=="":
            MessageBox.showinfo("Error!", "Por favor ingrese un usuario y su contraseña")
            
        else:
            coneccion = bd.connect()
            bandera = bd.consultaLogin(coneccion,user.get(),password.get())
            if bandera == True:
                frame = self.frames["MainMenu"]
                frame.tkraise()
            else:
                MessageBox.showinfo("Error!", "El usuario ingresado es incorrecto o no existe")
            
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        frame.clean_entries()
    
    def show_frameRegistrarVenta(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        frame.clean_entries()
        frame.rellenarProductos()






        

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
