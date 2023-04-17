import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as MessageBox
import ConexionBD as bd
import string
import random
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

        button_search = ctk.CTkButton(self, text="Buscar",
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

        

    def clean_entries(self):
        pass