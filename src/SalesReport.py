import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox
import ConexionBD as bd
import tkinter.font as font
from tkinter import *

class SalesReport(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")
        
        font_frame =  ctk.CTkFont(size=16)
        title_font_frame = ctk.CTkFont(size=26)
        font_label = font.Font(size=12)

        # Title
        label_title = ctk.CTkLabel(self, text="Reporte de Venta", 
                                   font=title_font_frame).place(x=10,y=10)
        
        #option menu
        self.period_time = ctk.CTkOptionMenu(self,
                                             font=font_frame,
                                             values=["Seleccione un periodo",
                                                     "Ultima semana",
                                                     "Ultimas dos semanas",
                                                     "Ultimo mes",
                                                     "Ultimos dos meses",
                                                     "Ultimos tres meses",
                                                     "Ultimos seis meses"])
        self.period_time.place(x=30,y=60)

        #start date entry
        label_start_date = ctk.CTkLabel(self, text="Fecha de inicio", 
                                   font=font_frame).place(x=30,y=110)
        self.entry_start_date = ctk.CTkEntry(self, width=190,
                                             height=30,
                                             border_width=2)
        self.entry_start_date.focus()
        self.entry_start_date.place(x=150,y=110)

        #end date entry
        label_end_date = ctk.CTkLabel(self, text="Fecha de fin", 
                                   font=font_frame).place(x=240+140,y=110)
        self.entry_end_date = ctk.CTkEntry(self, width=190,
                                             height=30,
                                             border_width=2)
        self.entry_end_date.focus()
        self.entry_end_date.place(x=360+120,y=110)

        button_search = ctk.CTkButton(self, text="Generar reporte",
                                      font=font_frame,
                                      width=60,
                                      height=20).place(x=720,y=112)
        
        #tree view information
        style = ttk.Style()
        style.theme_use('clam')

        self.tree = ttk.Treeview(self, column=("c0", "c1", "c2", "c3"), height=6)
        self.tree.column("# 0", anchor=CENTER)
        self.tree.heading("# 0", text="Codigo de factura")
        self.tree.column("# 1", anchor=CENTER)
        self.tree.heading("# 1", text="Fecha")
        self.tree.column("# 2", anchor=CENTER)
        self.tree.heading("# 2", text="Producto")
        self.tree.column("# 3", anchor=CENTER)
        self.tree.heading("# 3", text="Precio por unidad")
        self.tree.column("# 4", anchor=CENTER)
        self.tree.heading("# 4", text="Precio total de compra")
        self.tree.place(x=10,y=170)
        vsb = ttk.Scrollbar(self,orient = "vertical",command = self.tree.yview)
        vsb.place(x=1012, y=170, height=150)
        self.tree.configure(yscrollcommand=vsb.set)


        #report total entry
        label_end_date = ctk.CTkLabel(self, text="Total de periodo de ventas", 
                                   font=font_frame).place(x=630,y=350)

        self.entry_total_sale = ctk.CTkEntry(self, width=190,
                                             height=30,
                                             border_width=2)
        self.entry_total_sale.focus()
        self.entry_total_sale.place(x=830,y=350)

        # Generate PDF Button
        button_pdf = ctk.CTkButton(self,
                                  text="Generar PDF",
                                  font=font_frame,
                                  height=50,
                                  width=150)
        button_pdf.place(x=750, y=430)

        # Exit Button
        button_volver = ctk.CTkButton(self,
                                  text="Volver",
                                  font=font_frame,
                                  fg_color="#D61C1C",
                                  hover_color="#9E1818",
                                  height=50,
                                  width=150, 
                                  command=lambda:controller.show_frame("MainMenu"))
        button_volver.place(x=750, y=530)

    def clean_entries(self):
        pass