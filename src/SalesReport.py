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
        self.entry_start_date.insert(0,"Formato de fecha: año/mes/dia")
        self.entry_start_date.focus()
        self.entry_start_date.place(x=150,y=110)

        #end date entry
        label_end_date = ctk.CTkLabel(self, text="Fecha de fin", 
                                   font=font_frame).place(x=240+140,y=110)
        self.entry_end_date = ctk.CTkEntry(self, width=190,
                                             height=30,
                                             border_width=2)
        
        self.entry_end_date.insert(0,"Formato de fecha: año/mes/dia")
        self.entry_end_date.focus()
        self.entry_end_date.place(x=360+120,y=110)

        button_search = ctk.CTkButton(self, text="Generar reporte",
                                      font=font_frame,
                                      width=60,
                                      height=20,
                                      command = self.generarReporte).place(x=720,y=112)
        
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
        self.totalGanado = 0;

    def generarReporte(self):
        if self.period_time.get() == "Ultima semana":
            self.mostrarPeriodo(8,False)
        else:
            if self.period_time.get() == "Ultimas dos semanas":
                self.mostrarPeriodo(15,False)
            else:
                if self.period_time.get() == "Ultimo mes":
                    self.mostrarPeriodo(1,True)
                else:
                    if self.period_time.get() == "Ultimos dos meses":
                        self.mostrarPeriodo(2,True)
                    else:
                        if self.period_time.get() == "Ultimos tres meses":
                            self.mostrarPeriodo(3,True)
                        else:
                            if self.period_time.get() == "Ultimos seis meses":
                                self.mostrarPeriodo(6,True)
                            else:    
                                if self.entry_start_date.get() == "" or self.entry_end_date.get()=="":
                                    MessageBox.showinfo("Error!", "Por favor ingrese las fechas indicadas")
                                else:
                                    fechaInicio = self.entry_start_date.get()
                                    fechaFinal = self.entry_end_date.get()
                                    coneccion = bd.connect()
                                    bandera = bd.consultarFechas(coneccion,fechaInicio,fechaFinal)
                                    if bandera != "Nada":
                                        records = self.tree.get_children()
                                        for element in records:
                                            self.tree.delete(element)
                                        for row in bandera:
                                            cantidad = int(row[4])
                                            precio = int(row[3])
                                            total = precio * cantidad
                                            self.totalGanado = self.totalGanado + total
                                            self.tree.insert('', 0 , text= row[0],values = (row[1],row[2],row[3],total))
                                        self.entry_total_sale.insert(0,self.totalGanado)
                                    else:
                                        MessageBox.showinfo("Error!", "La fecha ingresada es incorrecta")

    def mostrarPeriodo(self,dias,esMes):
        self.clean_entries()
        coneccion = bd.connect()
        bandera = bd.consultaFechaPeriodo(coneccion,dias,esMes)
        if bandera != "Nada":
            records = self.tree.get_children()
            for element in records:
                self.tree.delete(element)
            for row in bandera:
                cantidad = int(row[4])
                precio = int(row[3])
                total = precio * cantidad
                self.totalGanado = self.totalGanado + total
                self.tree.insert('', 0 , text= row[0],values = (row[1],row[2],row[3],total))
            self.entry_total_sale.insert(0,self.totalGanado)
        else:
           MessageBox.showinfo("Error!", "La fecha ingresada es incorrecta") 
            
    def clean_entries(self):
        self.entry_start_date.delete(0, tk.END)
        self.entry_end_date.delete(0, tk.END)
        self.entry_total_sale.delete(0, tk.END)
        self.totalGanado = 0
        
        
