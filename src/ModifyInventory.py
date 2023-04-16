import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

import tkinter.font as font
from tkinter import *

class ModifyInventory(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        font_frame =  ctk.CTkFont(size=16)
        title_font_frame = ctk.CTkFont(size=26)

        # Title
        label_title = ctk.CTkLabel(self, text="Modificación de inventario", 
                                   font=title_font_frame).place(x=10,y=10)
        
        # Search fields
        label_search_name = ctk.CTkLabel(self, text="Filtro de nombre", 
                                         font=font_frame).place(x=150, y=50)
        self.entry_search_name= ctk.CTkEntry(self, font=font_frame, 
                                             width=500,
                                            height=30,
                                            border_width=2,)
        self.entry_search_name.focus()
        self.entry_search_name.place(x=280, y=50)
        self.buttonActionSearch = ctk.CTkButton(self, text="Buscar", 
                                                font=font_frame,
                                                width=100,
                                                height=20).place(x=800, y=55)
        
        # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        #Add TreeView widget
        self.tree = ttk.Treeview(self, column=("c0", "c1", "c2"))
        self.tree.column("# 0", anchor=CENTER)
        self.tree.heading("# 0", text="Codigo de producto")
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="Nombre del producto")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="Cantidad")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="Precio por unidad")
        self.tree.place(x=130,y=90)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.tree.yview)
        vsb.place(x=935, y=90, height=230)
        self.tree.configure(yscrollcommand=vsb.set)
        
        self.buttonSelect = ctk.CTkButton(self, text="Seleccionar", 
                                        font=font_frame, 
                                        fg_color="#17A926",
                                        hover_color="#0F6B18",).place(x=460, y=325)

        #Product code entry
        label_product_code = ctk.CTkLabel(self, text="Codigo de Producto", 
                                          font=font_frame).place(x=60,y=380)
        self.entry_product_code = ctk.CTkEntry(self, font=font_frame, 
                                            width=220,
                                            height=30,
                                            border_width=2,
                                            state="disabled")
        self.entry_product_code.focus()
        self.entry_product_code.place(x=220,y=380)
        
        #Product name entry
        label_product_name = ctk.CTkLabel(self, text="Nombre de Producto",
                                      font=font_frame).place(x=60,y=430)
        self.entry_product_name = ctk.CTkEntry(self, font=font_frame, 
                                            width=220,
                                            height=30,
                                            border_width=2)
        self.entry_product_name.focus()
        self.entry_product_name.place(x=220,y=430)
        
        #Product date entry
        label_product_date = ctk.CTkLabel(self, text="Fecha de vencimiento", 
                                          font=font_frame).place(x=60,y=480)
        self.entry_product_date = ctk.CTkEntry(self, font=font_frame, 
                                            width=220,
                                            height=30,
                                            border_width=2)
        self.entry_product_date.focus()
        self.entry_product_date.place(x=220,y=480)
        
        #Product brand entry
        label_product_brand = ctk.CTkLabel(self, text="Marca",
                                       font=font_frame).place(x=640,y=380)
        self.entry_product_brand = ctk.CTkEntry(self, font=font_frame, 
                                            width=220,
                                            height=30,
                                            border_width=2)
        self.entry_product_brand.focus()
        self.entry_product_brand.place(x=770,y=380)

        
        #Product quantity entry
        label_product_quantity = ctk.CTkLabel(self, text="Cantidad de producto", 
                                              font=font_frame).place(x=580,y=430)
        
        self.entry_product_quantity = ctk.CTkEntry(self, font=font_frame, 
                                            width=220,
                                            height=30,
                                            border_width=2)
        self.entry_product_quantity.focus()
        self.entry_product_quantity.place(x=770,y=430)

        self.buttonDecress = ctk.CTkButton(self, text="-", 
                                           font=font_frame,
                                           width=15).place(x=745, y=430)
        
        self.buttonIncrees = ctk.CTkButton(self, text="+", 
                                           font=font_frame,
                                           width=15).place(x=995, y=430)

              
        #Product price entry
        label_product_price = ctk.CTkLabel(self, text="Precio por unidad", 
                                           font=font_frame).place(x=600,y=480)
        self.entry_product_price = ctk.CTkEntry(self, font=font_frame, 
                                            width=220,
                                            height=30,
                                            border_width=2)
        self.entry_product_price.focus()
        self.entry_product_price.place(x=770,y=480)
        
        self.buttonModify = ctk.CTkButton(self, text="Modificar", 
                                          font=font_frame).place(x=150+50, y=550)
        
        self.buttonDelte = ctk.CTkButton(self, text="Eliminar",
                                     font=font_frame).place(x=300+50, y=550)
        
        self.buttonClean = ctk.CTkButton(self, text="Limpiar espacios", 
                                     font=font_frame).place(x=450+50, y=550)
        
        self.buttonExit = ctk.CTkButton(self, 
                                    text="Salir",
                                    fg_color="#D61C1C",
                                    hover_color="#9E1818", 
                                    font=font_frame,
                                    command=lambda: controller.show_frame("InventoryManagementMenu")).place(x=600+50, y=550)

    def clean_entries(self):
        pass
        self.entry_product_code.delete(0, tk.END)
        self.entry_product_name.delete(0, tk.END)
        self.entry_product_brand.delete(0, tk.END)
        self.entry_product_date.delete(0, tk.END)
        self.entry_product_quantity.delete(0, tk.END)
        self.entry_product_price.delete(0, tk.END)