import pyodbc

def connect():
    #Server Kevin Lanzas
    server = 'LAPTOP-N9RBF9JA\KEVIN1'
    database = 'LibreriaUniverso'
    username = 'sa'
    password = '12345sa'

    #Server Kevin Sanchez
    '''server = 'DESKTOP-KN8EIG1'
    database = 'LibreriaUniverso'
    username = 'sa'
    password = 'abc1234' '''
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return conn

# Ejecución de consulta
def consultaLogin(conn,user,contrasenia):
    try:
            cursor = conn.cursor()
            consulta = "SET NOCOUNT ON SELECT * FROM Usuarios WHERE Usuario = ? and Password = ?;"
            usuario = user
            key = contrasenia
            cursor.execute(consulta, (usuario,key))

            # Con fetchall traemos todas las filas
            
            Resultado = cursor.fetchall()
            if len(Resultado)<1:
                return False
            else:
                return True

            # Recorrer e imprimir
            for Res in Resultado: 
                print(Res)
                
    except Exception as e:
        print("Ocurrió un error al consultar con where: ", e)

def consultarCodigoFactura(conn,codigo):
    cursor = conn.cursor()
    consulta = "SET NOCOUNT ON SELECT * FROM Facturas WHERE [Codigo de Factura] = ?;"
    cursor.execute(consulta,(codigo))
    Resultado = cursor.fetchall()
    if len(Resultado)<1:
        return True
    else:
        return False

def consultaAgregarFactura(conn,codFactura,codProducto,producto,cantidad,precio,fecha,total):
    cursor = conn.cursor()
    consulta = "set ANSI_WARNINGS off INSERT INTO Facturas([Codigo de Factura],[Codigo de Producto],[Nombre del Producto],[Cantidad a Comprar],[Precio por unidad],Fecha,Total)VALUES(?,?,?,?,?,?,?);"
    cursor.execute(consulta,(codFactura,codProducto,producto,cantidad,precio,fecha,total))
    cursor.commit()

def disminuirCantidad(conn,codProducto,producto,cantidad):
    cursor = conn.cursor()
    consulta = "set ANSI_WARNINGS off UPDATE Productos SET [Cantidad Inicial] = [Cantidad Inicial] - ? WHERE Codigo = ? and Nombre = ?;"
    cursor.execute(consulta,(cantidad,codProducto,producto))
    cursor.commit()
    
    
def consultaVerificarCantidad(conn,codigo,cantidad,producto):
    cursor = conn.cursor()
    consulta = "SET NOCOUNT ON SELECT * FROM Productos WHERE Codigo = ? and Nombre = ? and [Cantidad Inicial] > ?;"
    cursor.execute(consulta,(codigo,producto,cantidad))
    Resultado = cursor.fetchall()
    if len(Resultado)<1:
        return False
    else:
        return True
    
def consultaPrecio(conn,codigo,producto):
    cursor = conn.cursor()
    consulta = "SET NOCOUNT ON SELECT Nombre,[Precio por Unidad] FROM Productos WHERE Codigo = ? and Nombre = ?;"
    cursor.execute(consulta,(codigo,producto))
    Resultado = cursor.fetchall()
    return Resultado

def consultaProducts(conn):
    try:
            cursor = conn.cursor()
            consulta = "SET NOCOUNT ON SELECT Codigo,Nombre,[Cantidad Inicial] FROM Productos;"
            cursor.execute(consulta)
            Resultado = cursor.fetchall()
            return Resultado
        
    except Exception as e:
        print("Ocurrió un error al consultar con where: ", e)

def consultaRegistrarProducto(conn,name,date,marca,quantity,price):
    try:
            cursor = conn.cursor()
            consulta = "set ANSI_WARNINGS off INSERT INTO Productos(Nombre,[Fecha de Vencimiento],Marca,[Cantidad Inicial],[Precio por unidad])VALUES(?,?,?,?,?);"
            nombre = name
            fecha = date
            marc = marca
            cantidad = quantity
            precio = price
            cursor.execute(consulta,(nombre,fecha,marc,cantidad,precio))
            cursor.commit()
                
    except Exception as e:
        print("Ocurrió un error al insertar: ", e)

            
# Cierre de conexión
def close():
    conn.close()
