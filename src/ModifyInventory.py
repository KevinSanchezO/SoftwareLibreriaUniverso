import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ConexionBD as bd
import tkinter.font as font
from tkinter import *

class ModifyInventory(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        
        font_title = font.Font(size=18, weight="bold")
        font_subtitle = font.Font(size=14, weight="bold")
        font_label = font.Font(size=12)

        # Title
        label_title = tk.Label(self, text="Modificación de inventario", font=font_title,
                               fg="white", bg="#252525").grid(row=0, column=0, 
                                columnspan=2, padx=10, pady=10, sticky="w")

        #Product code entry
        label_product_code = tk.Label(self, text="Codigo de Producto", font=font_label,
            fg="white", bg="#252525").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_code = tk.Entry(self, bg="#777777", 
            font=font_label, state='disabled').grid(row=1, column=1, padx=10, pady=10, sticky="e")

        #Product name entry
        label_product_name = tk.Label(self, text="Nombre de Producto", font=font_label,
            fg="white", bg="#252525").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_name = tk.Entry(self, bg="#777777", 
            font=font_label).grid(row=2, column=1, padx=10, pady=10, sticky="e")

        #Product date entry
        label_product_date = tk.Label(self, text="Fecha de vencimiento", font=font_label,
            fg="white", bg="#252525").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_date = tk.Entry(self, bg="#777777", 
            font=font_label).grid(row=3, column=1, padx=10, pady=10, sticky="e")

        #Product brand entry
        label_product_brand = tk.Label(self, text="Marca", font=font_label,
            fg="white", bg="#252525").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_brand = tk.Entry(self, bg="#777777", 
            font=font_label).grid(row=4, column=1, padx=10, pady=10, sticky="e")

        #Product quantity entry
        label_product_quantity = tk.Label(self, text="Cantidad de producto", font=font_label,
            fg="white", bg="#252525").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        
        self.entry_product_quantity = tk.Entry(self, bg="#777777", 
            font=font_label).grid(row=5, column=1, padx=10, pady=10, sticky="w")

        self.buttonDecress = tk.Button(self, text="-", font=font_label, bg="#1C66D6", 
            fg="white").place(x=169, y=238)
        
        self.buttonIncrees = tk.Button(self, text="+", font=font_label, bg="#1C66D6", 
            fg="white").place(x=375, y=238)
        
        #Product price entry
        label_product_price = tk.Label(self, text="Precio por unidad", font=font_label,
            fg="white", bg="#252525").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_price = tk.Entry(self, bg="#777777", 
            font=font_label).grid(row=6, column=1, padx=10, pady=10, sticky="e")

        # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        self.treeSelect = ttk.Treeview(self, column=("c0", "c1"))
        self.treeSelect.column("# 0", anchor=CENTER)
        self.treeSelect.heading("# 0", text="Codigo")
        self.treeSelect.column("# 1", anchor=CENTER)
        self.treeSelect.heading("# 1", text="Nombre")
        self.treeSelect.column("# 2", anchor=CENTER)
        self.treeSelect.heading("# 2", text="Cantidad")
        self.treeSelect.place(x=410,y=90)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.treeSelect.yview)
        vsb.place(x=1004, y=90, height=230)
        self.treeSelect.configure(yscrollcommand=vsb.set)

        label_search_code = tk.Label(self, text="Filtro de código", font=font_label,
            fg="white", bg="#252525").place(x=410, y=35)
        self.entry_search_code = tk.Entry(self, bg="#777777", 
            font=font_label).place(x=530, y=35)

        label_search_name = tk.Label(self, text="Filtro de nombre", font=font_label,
            fg="white", bg="#252525").place(x=410, y=65)
        self.entry_search_name= tk.Entry(self, bg="#777777", 
            font=font_label).place(x=530, y=65)
        
        self.buttonActionSearch = tk.Button(self, text="Buscar", font=font_label, bg="#1C66D6", 
            fg="white").place(x=950, y=55)

        self.buttonSelect = tk.Button(self, text="Seleccionar", font=font_label, bg="green", 
            fg="white").place(x=660, y=325)

        self.buttonModify = tk.Button(self, text="Modificar", font=font_label, bg="#1C66D6", 
            fg="white").place(x=50, y=360)
        
        self.buttonDelte = tk.Button(self, text="Eliminar", font=font_label, bg="#1C66D6", 
            fg="white").place(x=150, y=360)
        
        self.buttonClean = tk.Button(self, text="Limpiar\nespacios", font=font_label, bg="#1C66D6", 
            fg="white").place(x=250, y=350)
        
        self.buttonExit = tk.Button(self, text="Salir", font=font_label, bg="red", 
            fg="white", command=lambda: controller.show_frame("InventoryManagementMenu")).place(x=350, y=360)
   

    def clean_entries(self):
        pass
        #self.entry_product_code.delete(0, tk.END)
        #self.entry_product_name.delete(0, tk.END)
        #self.entry_product_brand.delete(0, tk.END)
        #self.entry_product_date.delete(0, tk.END)
        #self.entry_product_quantity.delete(0, tk.END)
        #self.entry_product_price.delete(0, tk.END)