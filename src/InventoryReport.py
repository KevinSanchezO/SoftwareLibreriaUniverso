import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox
import ConexionBD as bd
import tkinter.font as font
from tkinter import *
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors
from datetime import datetime

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
                                  width=150,
                                  command=self.generate_pdf)
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


    def obtener_datos(self):
        datos = [['Identificador', 'Nombre del producto', 'Marca', 'Cantidad en Stock']]
        for item in self.tree.get_children():
            text = self.tree.item(item)["text"]
            values = self.tree.item(item)["values"]
            cleaned_values = [text] + [value.strip() if isinstance(value, str) else value for value in values]
            datos.append(cleaned_values)
        print(datos)
        return datos


    def generate_pdf(self):
        # Obtener los datos del Treeview
        datos = self.obtener_datos()

        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        name_doc = 'ReporteInvetario_{}.pdf'.format(fecha_actual)

        # Crear el documento PDF
        doc = SimpleDocTemplate(name_doc, pagesize=letter)

        # Crear la tabla con los datos
        table = Table(datos)

        table.setStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, 0), 14),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black)
        ])

        # Agregar la tabla al documento
        elements = [table]
        doc.build(elements)

    def clean_entries(self):
        pass