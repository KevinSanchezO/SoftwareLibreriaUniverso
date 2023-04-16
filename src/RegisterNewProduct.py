import tkinter as tk
import customtkinter as ctk
import tkinter.font as font
from tkinter import *

class RegisterNewProduct(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        font_label = font.Font(size=12)

        font_frame =  ctk.CTkFont(size=18)
        title_font_frame = ctk.CTkFont(size=38)
        subtitle_font = ctk.CTkFont(size=28)

        label_title = ctk.CTkLabel(self, text="Menu de inicio", 
                            font=title_font_frame).place(x=30, y=30)

        # Subtitle
        label_subtitle = ctk.CTkLabel(self, text="Filtro de Registro",
                             font=subtitle_font).place(x=30, y=80)

        # Product Name Entry
        label_product_name = ctk.CTkLabel(self, text="Nombre de producto",
                                      font=font_frame).place(x=30+40, y=120+40)
        self.entry_product_name = ctk.CTkEntry(self, width=500,
                               height=30,
                               border_width=2, font=font_frame)
        self.entry_product_name.focus()
        self.entry_product_name.place(x=240+40,y=120+40)

        # Date Entry
        label_product_date = ctk.CTkLabel(self, text="Fecha de Vencimiento", 
                                      font=font_frame).place(x=30+40, y=170+40)
        self.entry_product_date = ctk.CTkEntry(self, width=500,
                               height=30,
                               border_width=2, font=font_frame)
        self.entry_product_date.focus()
        self.entry_product_date.place(x=240+40,y=170+40)

        # Marca Entry
        label_product_marca = ctk.CTkLabel(self, text="Marca", 
                                           font=font_frame).place(x=80+40,y=220+40)
        self.entry_product_marca = ctk.CTkEntry(self, width=500,
                               height=30,
                               border_width=2, font=font_frame)
        self.entry_product_marca.place(x=240+40,y=220+40)

        # Initial Quantity Entry
        label_initial_quantity = ctk.CTkLabel(self, text="Cantidad inicial", 
                                          font=font_frame).place(x=45+40, y=270+40)
        self.entry_initial_quantity = ctk.CTkEntry(self, width=500,
                               height=30,
                               border_width=2, font=font_frame)
        self.entry_initial_quantity.focus()
        self.entry_initial_quantity.place(x=240+40,y=270+40)

        # Initial Quantity Entry
        label_initial_price = ctk.CTkLabel(self, text="Precio por unidad", 
                                           font=font_frame).place(x=40+40,y=320+40)
        self.entry_initial_price = ctk.CTkEntry(self, width=500,
                               height=30,
                               border_width=2, font=font_frame)
        self.entry_initial_price.focus()
        self.entry_initial_price.place(x=240+40, y=320+40)

        # Save Button
        button_save = ctk.CTkButton(self, text="Guardar", 
                                    font=font_frame, 
                                    width=180,
                                    height=40,
            command=lambda:controller.verificationRegisterProduct(self.entry_product_name,
                            self.entry_product_date,self.entry_product_marca,
                            self.entry_initial_quantity,self.entry_initial_price))
        button_save.place(x=220,y=440)

        # Clean Button
        button_clean = ctk.CTkButton(self, text="Limpiar", 
                                    font=font_frame,
                                    width=180,
                                    height=40,
                                    command=self.clean_entries)
        button_clean.place(x=620,y=440)

        # Back Button
        back_button = ctk.CTkButton(self, 
                                    text="Salir", 
                                    font=font_frame,
                                    fg_color="#D61C1C",
                                    hover_color="#9E1818",
                                    width=180,
                                    height=40,
                                    command=lambda: controller.show_frame("InventoryManagementMenu"))
        back_button.place(x=780, y=80)

    def save_product(self):
        # Implement code to save the product here
        pass

    def clean_entries(self):
        self.entry_product_name.delete(0, tk.END)
        self.entry_initial_price.delete(0, tk.END)
        self.entry_initial_quantity.delete(0, tk.END)
        self.entry_product_date.delete(0, tk.END)
        self.entry_product_marca.delete(0, tk.END)
        pass