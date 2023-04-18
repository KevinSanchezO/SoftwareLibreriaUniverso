import tkinter as tk
import customtkinter as ctk
from tkinter import *
from PIL import Image,ImageTk

class MainMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        font_frame =  ctk.CTkFont(size=18)
        title_font_frame = ctk.CTkFont(size=38)

        label_title = ctk.CTkLabel(self, text="Menu de inicio", 
                            font=title_font_frame).place(x=30, y=30)
        
        #Imagen de Generar Reporte de Inventario
        global imagenGenerarReporteInventario
        imgGenerarReporteInventario = Image.open("images//GenerarReporteInventario.png")
        imgGenerarReporteInventario = imgGenerarReporteInventario.resize((100,100),Image.LANCZOS)
        imagenGenerarReporteInventario = ImageTk.PhotoImage(imgGenerarReporteInventario)
        lblImagen=Label(self,image=imagenGenerarReporteInventario,bg="#252525").place(x=115,y=190)

        #Imagen Reporte de Ventas
        global imagenGenerarReporteVentas
        imgGenerarReporteVenta = Image.open("images//GenerarReporteVenta.png")
        imgGenerarReporteVenta = imgGenerarReporteVenta.resize((100,100),Image.LANCZOS)
        imagenGenerarReporteVentas = ImageTk.PhotoImage(imgGenerarReporteVenta)
        lblImagen=Label(self,image=imagenGenerarReporteVentas,bg="#252525").place(x=360,y=190)

        #Imagen Registrar Venta
        global imagenRegistrarVenta
        imgRegistrarVenta = Image.open("images//RegistrarVenta.png")
        imgRegistrarVenta = imgRegistrarVenta.resize((100,100),Image.LANCZOS)
        imagenRegistrarVenta = ImageTk.PhotoImage(imgRegistrarVenta)
        lblImagen=Label(self,image=imagenRegistrarVenta,bg="#252525").place(x=600,y=190)

        #Imagen Mantenimiento de Inventario
        global imagenMantenimientoInventario
        imgMantenimientoInventario = Image.open("images//MantenimientoInventario.png")
        imgMantenimientoInventario = imgMantenimientoInventario.resize((100,100),Image.LANCZOS)
        imagenMantenimientoInventario = ImageTk.PhotoImage(imgMantenimientoInventario)
        lblImagen=Label(self,image=imagenMantenimientoInventario,bg="#252525").place(x=820,y=190)

        # Add the menu buttons to this frame  Reporte Inventario
        button1 = ctk.CTkButton(self, text="Reporte Inventario", font=font_frame, height=36,
                                command=lambda: controller.show_frame("InventoryReport"))

        button2 = ctk.CTkButton(self, text="Reporte Ventas", font=font_frame, height=36,
                                command=lambda: controller.show_frame("SalesReport"))
        
        button3 = ctk.CTkButton(self, text="Registrar Venta", font=font_frame, height=36,
                    command=lambda: controller.show_frameRegistrarVenta("RegistrarVenta"))
        
        button4 = ctk.CTkButton(self, text="Mantenimiento\nInventario", font=font_frame, height=36,
                            command=lambda: controller.show_frame("InventoryManagementMenu"))

        # Arrange the buttons in a single row with a padding of 80 pixels
        button1.place(x=90,y=310)
        button2.place(x=340,y=310)
        button3.place(x=580,y=310)
        button4.place(x=802,y=300)

        # Add a back button to return to the login screen
        back_button = ctk.CTkButton(self, 
                                    text="Salir", 
                                    font=font_frame,
                                    fg_color="#D61C1C",
                                    hover_color="#9E1818",
                                    command=lambda: controller.show_frame("LogIn"))
        back_button.place(x=450,y=400)

    def clean_entries(self):
        pass