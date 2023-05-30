import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox
import ConexionBD as bd
import tkinter.font as font
from tkinter import *

class InventoryReport(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        
        font_frame =  ctk.CTkFont(size=16)
        title_font_frame = ctk.CTkFont(size=26)
        font_label = font.Font(size=12)

        # Title
        label_title = ctk.CTkLabel(self, text="Reporte de Inventario", 
                                   font=title_font_frame).place(x=10,y=10)
        
        #minimun info to work
        label_search_ammount = ctk.CTkLabel(self, text="Solicitar productos con\n stock menor o igual a:", 
                                   font=font_frame).place(x=30,y=70)
        self.entry_search_ammount = ctk.CTkEntry(self, width=100,
                                             height=30,
                                             border_width=2)
        self.entry_search_ammount.focus()
        self.entry_search_ammount.place(x=210,y=75)

        #button create report with minimun info
        button_search = ctk.CTkButton(self, text="Generar reporte por\nconsulta",
                                      font=font_frame,
                                      width=60,
                                      height=20,
                                      command=self.request_stock).place(x=200,y=145)
        
        #button create report with minimun info
        button_search_zero = ctk.CTkButton(self, text="Generar reporte de\nproductos sin stock",
                                      font=font_frame,
                                      width=60,
                                      height=20,
                                      command=self.request_stock_zero).place(x=650,y=145)
        
        # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use('clam')

        #Add TreeView widget
        self.tree = ttk.Treeview(self, column=("c0", "c1", "c2"), height=12)
        self.tree.column("# 0", anchor=CENTER)
        self.tree.heading("# 0", text="Codigo de producto")
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="Nombre del producto")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="Marca")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="Cantidad")
        self.tree.place(x=100,y=230)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.tree.yview)
        vsb.place(x=905, y=231, height=268)
        self.tree.configure(yscrollcommand=vsb.set)

        # Generate PDF Button
        button_pdf = ctk.CTkButton(self,
                                  text="Generar PDF",
                                  font=font_frame,
                                  height=40,
                                  width=150)
        button_pdf.place(x=200, y=540)

        # Exit Button
        button_volver = ctk.CTkButton(self,
                                  text="Volver",
                                  font=font_frame,
                                  fg_color="#D61C1C",
                                  hover_color="#9E1818",
                                  height=40,
                                  width=150, 
                                  command=lambda:controller.show_frame("MainMenu"))
        button_volver.place(x=650, y=540)

    def request_stock(self):
        coneccion = bd.connect()
        if self.entry_search_ammount.get().isdigit():

            bandera = bd.consultar_productos_stock(coneccion, self.entry_search_ammount.get())

            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            for row in bandera:
                self.tree.insert('', 0 , text= row[0],values = (row[1],row[2],row[3]))


    def request_stock_zero(self):
        coneccion = bd.connect()

        bandera = bd.consultar_productos_stock(coneccion, 0)

        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        for row in bandera:
                self.tree.insert('', 0 , text= row[0],values = (row[1],row[2],row[3]))


    def clean_entries(self):
        pass