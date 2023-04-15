import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox
import ConexionBD as bd
import string
import random
import tkinter.font as font
from tkinter import *
from PIL import Image,ImageTk

class RegistrarVenta(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        
        font_title = font.Font(size=18, weight="bold")
        font_subtitle = font.Font(size=14, weight="bold")
        font_label = font.Font(size=12)

        # Title
        label_title = tk.Label(self, text="Registrar Venta", font=font_title,
                               fg="white", bg="#252525")
        label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Subtitle
        label_subtitle = tk.Label(self, text="Filtro de venta", font=font_subtitle,
                                  fg="white", bg="#252525")
        label_subtitle.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        #Codigo de Factura Entry
        label_product_codeFactura = tk.Label(self, text="Codigo de Factura", font=font_label,
                                      fg="white", bg="#252525")
        label_product_codeFactura.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_codeFactura = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_codeFactura.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Name Product Entry
        label_product_nameProduct = tk.Label(self, text="Nombre del Producto", font=font_label,
                                      fg="white", bg="#252525")
        label_product_nameProduct.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_nameProduct = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_nameProduct.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Code Product Entry
        label_product_codeProduct = tk.Label(self, text="Codigo del producto", font=font_label,
                                      fg="white", bg="#252525")
        label_product_codeProduct.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_codeProduct = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_codeProduct.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        # Quantity Entry
        label_product_quantity = tk.Label(self, text="Cantidad a vender", font=font_label,
                                           fg="white", bg="#252525")
        label_product_quantity.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_quantity = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_quantity.grid(row=4, column=1, padx=10, pady=10, sticky="e")

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
        self.treeSelect.place(x=400,y=10)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.treeSelect.yview)
        vsb.place(x=450+200+2+200+2+150, y=10, height=200+30)
        self.treeSelect.configure(yscrollcommand=vsb.set)
        
        button_Select = tk.Button(self, text="Seleccionar", font=font_label, bg="green", fg="white",
                                  command= self.seleccionarItem)
        button_Select.place(x=650,y=240)
        
        #Total Entry
        label_product_Total = tk.Label(self, text="Total", font=font_label,fg="white", bg="#252525")
        label_product_Total.place(x=810,y=360)
        self.entry_product_Total = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_Total.insert(0,"0")
        self.entry_product_Total.place(x=850,y=360)

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
        self.tree.place(x=0,y=290)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.tree.yview)
        vsb.place(x=0+200+2+200+2+150+235, y=292, height=140)
        self.tree.configure(yscrollcommand=vsb.set)
        #self.rellenarProductos()
        button_Select = tk.Button(self, text="Realizar Pago", font=font_label, bg="green", fg="white",
                                  command= self.RealizarPago)
        button_Select.place(x=810,y=400)
        
        # Save Button
        
        button_save = tk.Button(self, text="Agregar", font=font_label, bg="green", fg="white",
                                command = self.agregarFactura)
        button_save.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Clean Button
        button_clean = tk.Button(self, text="Limpiar Venta", font=font_label, bg="gray", fg="#FFFFFF", 
                                 command=self.clean_entries)
        button_clean.place(x=160,y=240)

        # Exit Button
        button_volver = tk.Button(self, text="Volver", font=font_label, bg="#D61C1C", fg="white",
                                 command=lambda:controller.show_frame("MainMenu"))
        button_volver.place(x=330,y=240)

    def RealizarPago(self):
        for child in self.tree.get_children():
            coneccion = bd.connect()
            bandera = bd.consultaAgregarFactura(coneccion,self.entry_product_codeFactura.get(),self.tree.item(child)["text"],self.tree.item(child)["values"][0],self.tree.item(child)["values"][1],self.tree.item(child)["values"][2],"0",self.entry_product_Total.get())
            bd.disminuirCantidad(coneccion,self.tree.item(child)["text"],self.tree.item(child)["values"][0],self.tree.item(child)["values"][1])
        self.rellenarProductos()
        
        MessageBox.showinfo("Aviso!", "Compra registrada con Exito")

    def reset(self):
        self.clean_entries()
        self.entry_product_Total.delete(0, tk.END)
        self.entry_product_Total.insert(0,"0")
        self.entry_product_codeFactura.config(state='normal')
        self.entry_product_codeFactura.delete(0, tk.END)
        self.crearCodFactura()
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
            
    def agregarFactura(self):
        if self.entry_product_codeProduct.get() == "" or self.entry_product_nameProduct.get()=="" or self.entry_product_quantity.get()=="":
            MessageBox.showinfo("Error!", "Por favor ingrese los datos que se le solicitan")
        else:
            coneccion = bd.connect()
            bandera = bd.consultaVerificarCantidad(coneccion,self.entry_product_codeProduct.get(),self.entry_product_quantity.get(),self.entry_product_nameProduct.get())
            if bandera == True:
                coneccion = bd.connect()
                precio = bd.consultaPrecio(coneccion,self.entry_product_codeProduct.get(),self.entry_product_nameProduct.get())
                for row in precio:
                    self.tree.insert('', 0 , text=self.entry_product_codeProduct.get() ,values = (self.entry_product_nameProduct.get(),self.entry_product_quantity.get(),row[1]))
                    totalActual = int(self.entry_product_Total.get())
                    self.entry_product_Total.delete(0, tk.END)
                    compra = int(row[1])
                    cantidad = int(self.entry_product_quantity.get())
                    total = totalActual + (compra * cantidad)
                    self.entry_product_Total.insert(0, total)    
            else:
                MessageBox.showinfo("Error!", "Los datos son incorrectos")
                
    def seleccionarItem(self):
        try:
            self.clean_entries()
            self.entry_product_codeProduct.insert(0,self.treeSelect.item(self.treeSelect.selection())['text'])
            self.entry_product_nameProduct.insert(0,self.treeSelect.item(self.treeSelect.selection())['values'][0])
        except IndexError as e:
            MessageBox.showinfo("Error!", "Por favor seleccione algun elemento")
            
    def rellenarProductos(self):
        self.reset()
        self.crearCodFactura()
        #Coneccion y realizar consulta a la base de datos
        records = self.treeSelect.get_children()
        for element in records:
            self.treeSelect.delete(element)
        coneccion = bd.connect()
        productos = bd.consultaProducts(coneccion)
        # Recorrer e imprimir
        for row in productos:
            self.treeSelect.insert('', 0 , text= row[0],values = (row[1],row[2]))
            
    def crearCodFactura(self):
        #Generador de codigo de factura aleatorio
        number_of_strings = 1
        length_of_string = 6
        for x in range(number_of_strings):
            codigo = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
            coneccion = bd.connect()
            bandera = bd.consultarCodigoFactura(coneccion,codigo)
            if bandera == True: 
                self.entry_product_codeFactura.insert(0,codigo)
                self.entry_product_codeFactura.config(state='disabled')
            
    def clean_entries(self):
        self.entry_product_nameProduct.delete(0, tk.END)
        self.entry_product_codeProduct.delete(0, tk.END)
        self.entry_product_quantity.delete(0, tk.END)
        pass