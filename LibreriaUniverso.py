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

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the geometry of the main window
        self.geometry("1040x680")

        # Create the container frame
        self.container = tk.Frame(self, bg="#252525")
        self.container.pack(fill="both", expand=True)

        # Create the header frame
        self.header = tk.Frame(self.container, bg="#252525", height=50)
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
        self.frames = {}
        for F in (LogIn, MainMenu, InventoryManagementMenu, RegisterNewProduct, 
                  RegistrarVenta, ModifyInventory):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        # Show the first frame
        self.show_frame(RegistrarVenta)

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
                frame = self.frames[LogIn]
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
                  
class LogIn(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        parent.config(width=200,height=200) 
        font_frame = font.Font(size=12)

        # Add the login widgets to this frame
        label_username = tk.Label(self, text="Username", font=font_frame,
                        fg="white", bg="#252525").grid(row=0, 
                        column=0, padx=10, pady=10, sticky="w")
        self.entry_username = tk.Entry(self, bg="#777777", fg="black", font=font_frame)
        self.entry_username.focus()
        self.entry_username.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        label_password = tk.Label(self, text="Password", font=font_frame,
                        fg="white", bg="#252525").grid(row=1, 
                        column=0, padx=10, pady=10, sticky="w")
        
        self.entry_password = tk.Entry(self, show="*", bg="#777777", fg="black", font=font_frame)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        button_1 = tk.Button(self, text="Ingresar", bg="#1C66D6", fg="white", font=font_frame,
                    command=lambda: controller.verification(self.entry_username,self.entry_password)).grid(row=2,
                    column=0, columnspan=2, padx=10, pady=10)#controller.show_frame(MainMenu)).grid(row=2,
                    #column=0, columnspan=2, padx=10, pady=10)

    def clean_entries(self):
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

class MainMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        
        #Imagen de Generar Reporte de Inventario
        global imagenGenerarReporteInventario
        imgGenerarReporteInventario = Image.open("images//GenerarReporteInventario.png")
        imgGenerarReporteInventario = imgGenerarReporteInventario.resize((100,100),Image.LANCZOS)
        imagenGenerarReporteInventario = ImageTk.PhotoImage(imgGenerarReporteInventario)
        lblImagen=Label(self,image=imagenGenerarReporteInventario,bg="#252525").place(x=68,y=90)

        #Imagen Reporte de Ventas
        global imagenGenerarReporteVentas
        imgGenerarReporteVenta = Image.open("images//GenerarReporteVenta.png")
        imgGenerarReporteVenta = imgGenerarReporteVenta.resize((100,100),Image.LANCZOS)
        imagenGenerarReporteVentas = ImageTk.PhotoImage(imgGenerarReporteVenta)
        lblImagen=Label(self,image=imagenGenerarReporteVentas,bg="#252525").place(x=300,y=90)

        #Imagen Registrar Venta
        global imagenRegistrarVenta
        imgRegistrarVenta = Image.open("images//RegistrarVenta.png")
        imgRegistrarVenta = imgRegistrarVenta.resize((100,100),Image.LANCZOS)
        imagenRegistrarVenta = ImageTk.PhotoImage(imgRegistrarVenta)
        lblImagen=Label(self,image=imagenRegistrarVenta,bg="#252525").place(x=525,y=90)

        #Imagen Mantenimiento de Inventario
        global imagenMantenimientoInventario
        imgMantenimientoInventario = Image.open("images//MantenimientoInventario.png")
        imgMantenimientoInventario = imgMantenimientoInventario.resize((100,100),Image.LANCZOS)
        imagenMantenimientoInventario = ImageTk.PhotoImage(imgMantenimientoInventario)
        lblImagen=Label(self,image=imagenMantenimientoInventario,bg="#252525").place(x=775,y=90)

        button_font = font.Font(size=12)

        # Add the menu buttons to this frame
        button1 = tk.Button(self, text="Reporte Inventario", font=button_font, 
                            bg="#1C66D6", fg="white")
        button2 = tk.Button(self, text="Reporte Ventas", font=button_font, 
                            bg="#1C66D6", fg="white")
        button3 = tk.Button(self, text="Registrar Venta", font=button_font, 
                            bg="#1C66D6", fg="white",command=lambda: controller.show_frameRegistrarVenta(RegistrarVenta))
        button4 = tk.Button(self, text="Mantenimiento Inventario", 
                            font=button_font, bg="#1C66D6", fg="white",
                            command=lambda: controller.show_frame(InventoryManagementMenu))

        # Arrange the buttons in a single row with a padding of 80 pixels
        button1.pack(side="left", padx=50, pady=200)
        button2.pack(side="left", padx=50, pady=200)
        button3.pack(side="left", padx=50, pady=200)
        button4.pack(side="left", padx=50, pady=200)

        # Add a back button to return to the login screen
        back_button = tk.Button(self, text="Salir", bg="#D61C1C", 
                                fg="white", font=button_font,
                                command=lambda: controller.show_frame(LogIn))
        back_button.pack(side="bottom")

    def clean_entries(self):
        pass

class InventoryManagementMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        #Imagen registrar producto
        global imagenRegistrar
        imgRegistrar = Image.open("images//register.png")
        imgRegistrar = imgRegistrar.resize((100,100),Image.LANCZOS)
        imagenRegistrar = ImageTk.PhotoImage(imgRegistrar)
        lblImagenRegistrar=Label(self,image=imagenRegistrar,bg="#252525").place(x=200,y=90)

        #Imagen Inventario
        global imagenInventario
        imgInventario = Image.open("images//Inventario.png")
        imgInventario = imgInventario.resize((100,100),Image.LANCZOS)
        imagenInventario = ImageTk.PhotoImage(imgInventario)
        lblImagen=Label(self,image=imagenInventario,bg="#252525").place(x=640,y=90)
        
        font_frame = font.Font(size=12)

        # Add the menu buttons to this frame
        button1 = tk.Button(self, text="Registrar nuevo producto", 
                            font=font_frame, bg="#1C66D6", fg="white",
                            command=lambda: controller.show_frame(RegisterNewProduct))
        button2 = tk.Button(self, text="Ver inventario", 
                            font=font_frame, bg="#1C66D6", fg="white",
                            command=lambda: controller.show_frame(ModifyInventory))

        # Arrange the buttons in a single row with a padding of 80 pixels
        button1.pack(side="left", padx=150, pady=200)
        button2.pack(side="left", padx=150, pady=200)

        # Add a back button to return to the login screen
        back_button = tk.Button(self, text="Salir", bg="#D61C1C", 
                                fg="white", font=font_frame,
                                command=lambda: controller.show_frame(MainMenu))
        back_button.pack(side="bottom")

    def clean_entries(self):
        pass

class RegisterNewProduct(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        font_title = font.Font(size=18, weight="bold")
        font_subtitle = font.Font(size=14, weight="bold")
        font_label = font.Font(size=12)

        # Title
        label_title = tk.Label(self, text="Registrar nuevo producto", font=font_title,
                               fg="white", bg="#252525")
        label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        # Subtitle
        label_subtitle = tk.Label(self, text="Filtro de registro", font=font_subtitle,
                                  fg="white", bg="#252525")
        label_subtitle.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Product Name Entry
        label_product_name = tk.Label(self, text="Nombre de producto", font=font_label,
                                      fg="white", bg="#252525")
        label_product_name.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_name = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_name.focus()
        self.entry_product_name.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Date Entry
        label_product_date = tk.Label(self, text="Fecha de Vencimiento", font=font_label,
                                      fg="white", bg="#252525")
        label_product_date.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_date = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_date.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        # Marca Entry
        label_product_marca = tk.Label(self, text="Marca", font=font_label,
                                      fg="white", bg="#252525")
        label_product_marca.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entry_product_marca = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_product_marca.grid(row=5, column=1, padx=10, pady=10, sticky="e")

        # Initial Quantity Entry
        label_initial_quantity = tk.Label(self, text="Cantidad inicial", font=font_label,
                                           fg="white", bg="#252525")
        label_initial_quantity.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.entry_initial_quantity = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_initial_quantity.grid(row=6, column=1, padx=10, pady=10, sticky="e")

        # Initial Quantity Entry
        label_initial_price = tk.Label(self, text="Precio por unidad", font=font_label,
                                           fg="white", bg="#252525")
        label_initial_price.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.entry_initial_price = tk.Entry(self, bg="#777777", font=font_label)
        self.entry_initial_price.grid(row=7, column=1, padx=10, pady=10, sticky="e")

        # Save Button
        button_save = tk.Button(self, text="Guardar", font=font_label, bg="green", fg="white",
                                command=lambda:controller.verificationRegisterProduct(self.entry_product_name,self.entry_product_date,self.entry_product_marca,
                                                                                      self.entry_initial_quantity,self.entry_initial_price))
        button_save.grid(row=8, column=0, padx=10, pady=10, sticky="w")

        # Clean Button
        button_clean = tk.Button(self, text="Limpiar", font=font_label, bg="gray", fg="#FFFFFF",
                                 command=self.clean_entries)
        button_clean.grid(row=8, column=1, padx=10, pady=10, sticky="e")

        # Clean Button
        button_volver = tk.Button(self, text="Volver", font=font_label, bg="#D61C1C", fg="white",
                                 command=lambda: controller.show_frame(InventoryManagementMenu))
        button_volver.grid(row=8, column=2, padx=10, pady=10, sticky="e")

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
                                 command=lambda:controller.show_frame(MainMenu))
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
            fg="white", command=lambda: controller.show_frame(InventoryManagementMenu)).place(x=350, y=360)
   

    def clean_entries(self):
        pass
        #self.entry_product_code.delete(0, tk.END)
        #self.entry_product_name.delete(0, tk.END)
        #self.entry_product_brand.delete(0, tk.END)
        #self.entry_product_date.delete(0, tk.END)
        #self.entry_product_quantity.delete(0, tk.END)
        #self.entry_product_price.delete(0, tk.END)
        

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
