import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox
import ConexionBD as bd
import string
import random
import tkinter.font as font
from tkinter import *

class RegistrarVenta(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        
        font_frame =  ctk.CTkFont(size=16)
        title_font_frame = ctk.CTkFont(size=26)
        font_label = font.Font(size=12)

        # Title
        label_title = ctk.CTkLabel(self, text="Registrar Venta", 
                                   font=title_font_frame).place(x=30,y=30)

        #Codigo de Factura Entry
        label_product_codeFactura = ctk.CTkLabel(self, text="Codigo de Factura", 
                                             font=font_frame).place(x=30,y=70)
        self.entry_product_codeFactura = ctk.CTkEntry(self, font=font_frame, 
                                                      width=190,
                                                      height=30,
                                                      border_width=2)
        self.entry_product_codeFactura.focus()
        self.entry_product_codeFactura.place(x=200,y=70)

        # Name Product Entry
        label_product_nameProduct = ctk.CTkLabel(self, text="Nombre del Producto",
                                             font=font_frame).place(x=30,y=110)
        self.entry_product_nameProduct = ctk.CTkEntry(self, font=font_frame, 
                                                      width=190,
                                                      height=30,
                                                      border_width=2)
        self.entry_product_nameProduct.focus()
        self.entry_product_nameProduct.place(x=200,y=110)

        # Code Product Entry
        label_product_codeProduct = ctk.CTkLabel(self, text="Codigo del producto", 
                                                 font=font_frame).place(x=30,y=150)
        self.entry_product_codeProduct = ctk.CTkEntry(self, font=font_frame, 
                                                      width=190,
                                                      height=30,
                                                      border_width=2)
        self.entry_product_codeProduct.focus()
        self.entry_product_codeProduct.place(x=200,y=150)

        # Quantity Entry
        label_product_quantity = ctk.CTkLabel(self, text="Cantidad a vender", 
                                          font=font_frame).place(x=30,y=190)

        self.entry_product_quantity = ctk.CTkEntry(self, font=font_frame, 
                                                      width=190,
                                                      height=30,
                                                      border_width=2)
        self.entry_product_quantity.focus()
        self.entry_product_quantity.place(x=200,y=190)

        # Search fields
        label_search_name = ctk.CTkLabel(self, text="Filtro de nombre", 
                                         font=font_frame).place(x=410, y=40)
        self.entry_search_name= ctk.CTkEntry(self, font=font_frame, 
                                             width=400,
                                            height=30,
                                            border_width=2,)
        self.entry_search_name.focus()
        self.entry_search_name.place(x=530, y=40)

        
        self.buttonActionSearch = ctk.CTkButton(self, text="Buscar", 
                                                font=font_frame,
                                                width=60,
                                                height=20).place(x=950, y=45)
        

        # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        self.treeSelect = ttk.Treeview(self, column=("c0", "c1"), height=6)
        self.treeSelect.column("# 0", anchor=CENTER)
        self.treeSelect.heading("# 0", text="Codigo")
        self.treeSelect.column("# 1", anchor=CENTER)
        self.treeSelect.heading("# 1", text="Nombre")
        self.treeSelect.column("# 2", anchor=CENTER)
        self.treeSelect.heading("# 2", text="Cantidad")
        self.treeSelect.place(x=400,y=80)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.treeSelect.yview)
        vsb.place(x=1004, y=80, height=150)
        self.treeSelect.configure(yscrollcommand=vsb.set)
        
        button_Select = ctk.CTkButton(self,
                                      text="Seleccionar", 
                                      font=font_frame,
                                      command= self.seleccionarItem)
        button_Select.place(x=650,y=245)
        
        #Total Entry
        label_product_Total = ctk.CTkLabel(self,
                                           text="Total",
                                           font=font_frame).place(x=370, y=530)
        self.entry_product_Total = ctk.CTkEntry(self, font=font_frame,
                                                width=190,
                                                height=30,
                                                border_width=2)
        self.entry_product_Total.insert(0,"0")
        self.entry_product_Total.place(x=430,y=530)

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
        self.tree.place(x=100,y=290)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.tree.yview)
        vsb.place(x=905, y=291, height=228)
        self.tree.configure(yscrollcommand=vsb.set)
        self.rellenarProductos()
        
        # Save Button
        button_save = ctk.CTkButton(self,
                                    text="Agregar",
                                    font=font_frame,
                                    fg_color="#17A926",
                                    hover_color="#0F6B18",
                                    width=100,
                                    command = self.agregarFactura).place(x=50,y=242)

        # Clean Button
        button_clean = ctk.CTkButton(self, text="Limpiar Venta",
                                     font=font_frame,
                                     width=100,
                                     command=self.clean_entries).place(x=240,y=242)


        button_make_sale = ctk.CTkButton(self,
                                      text="Realizar Pago",
                                      font=font_frame,
                                      fg_color="#17A926",
                                      hover_color="#0F6B18",
                                      command= self.RealizarPago)
        button_make_sale.place(x=220, y=570)

        # Exit Button
        button_volver = ctk.CTkButton(self,
                                  text="Volver",
                                  font=font_frame,
                                  fg_color="#D61C1C",
                                  hover_color="#9E1818", 
                                  command=lambda:controller.show_frame("MainMenu"))
        button_volver.place(x=650, y=570)

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
        self.entry_product_codeFactura.configure(state='normal')
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
                self.entry_product_codeFactura.configure(state='disabled')
            
    def clean_entries(self):
        self.entry_product_nameProduct.delete(0, tk.END)
        self.entry_product_codeProduct.delete(0, tk.END)
        self.entry_product_quantity.delete(0, tk.END)
        pass