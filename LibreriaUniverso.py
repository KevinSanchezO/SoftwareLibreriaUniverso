import tkinter as tk
import customtkinter as ctk
import os
import ConexionBD as bd
from PIL import Image
import tkinter.font as font

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
        for F in (LogIn, MainMenu, InventoryManagementMenu):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        # Show the first frame
        self.show_frame(MainMenu)

    def verification(self,user,password):
        if user.get() == "" or password.get()=="":
            print("Por favor ingrese un usuario y su contraseña")
        else:
            bandera = bd.consultaLogin(user.get(),password.get())
            if bandera == True:
                frame = self.frames[MainMenu]
                frame.tkraise()
            else:
                print("Usuario no encontrado")
            
    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()
        frame.clean_entries()
                
        
class LogIn(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#252525")

        font_frame = font.Font(size=12)

        # Add the login widgets to this frame
        label_username = tk.Label(self, text="Username", font=font_frame,
                        fg="white", bg="#252525").grid(row=0, 
                        column=0, padx=10, pady=10, sticky="w")
        self.entry_username = tk.Entry(self, bg="white", font=font_frame)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        label_password = tk.Label(self, text="Password", font=font_frame,
                        fg="white", bg="#252525").grid(row=1, 
                        column=0, padx=10, pady=10, sticky="w")
        
        self.entry_password = tk.Entry(self, show="*", bg="white", font=font_frame)
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
    
        button_font = font.Font(size=12)

        # Add the menu buttons to this frame
        button1 = tk.Button(self, text="Reporte Inventario", font=button_font, 
                            bg="#1C66D6", fg="white")
        button2 = tk.Button(self, text="Reporte Ventas", font=button_font, 
                            bg="#1C66D6", fg="white")
        button3 = tk.Button(self, text="Registrar Venta", font=button_font, 
                            bg="#1C66D6", fg="white")
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
        font_frame = font.Font(size=12)

        # Add the menu buttons to this frame
        button1 = tk.Button(self, text="Registrar nuevo producto", 
                            font=font_frame, bg="#1C66D6", fg="white")
        button2 = tk.Button(self, text="Ver inventario", 
                            font=font_frame, bg="#1C66D6", fg="white")

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
        font_frame = font.Font(size=12)

        label_product_name = tk.Label(self, text="Nombre de producto", font=font_frame,
                        fg="white", bg="#252525").grid(row=0, 
                        column=0, padx=10, pady=10, sticky="w")
        self.entry_username = tk.Entry(self, bg="white", font=font_frame)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10, sticky="e")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
