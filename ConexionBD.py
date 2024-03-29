import pyodbc

def connect():
    #Server Kevin Lanzas
    server = 'LAPTOP-N9RBF9JA\KEVIN1'
    database = 'LibreriaUniverso'
    username = 'sa'
    password = '12345sa'
    

    #Server Kevin Sanchez
    '''
    server = 'DESKTOP-KN8EIG1'
    database = 'LibreriaUniverso'
    username = 'sa'
    password = 'abc1234'
    '''
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

def consultarFechas(conn,fechaInicio,fechaFinal):
    try:
            cursor = conn.cursor()
            consulta = "SELECT [Codigo de Factura],Fecha,[Nombre del Producto],[Precio por Unidad],[Cantidad a Comprar] FROM Facturas WHERE fecha  BETWEEN ? AND ? ORDER BY [Codigo de Factura];"
            cursor.execute(consulta, (fechaInicio,fechaFinal))

            # Con fetchall traemos todas las filas
            
            Resultado = cursor.fetchall()
            if len(Resultado)<1:
                return "Nada"
            else:
                return Resultado
                
    except Exception as e:
        print("Ocurrió un error al consultar con where: ", e)

def consultaFechaPeriodo(conn,dias,esMes):
    try:
        if esMes == False:
            cursor = conn.cursor()
            consulta = "SELECT [Codigo de Factura],Fecha,[Nombre del Producto],[Precio por Unidad],[Cantidad a Comprar] FROM Facturas WHERE [Fecha] >= dateadd (dd, -?, getdate());"
            cursor.execute(consulta, (dias))
            # Con fetchall traemos todas las filas
            Resultado = cursor.fetchall()
            if len(Resultado)<1:
                return "Nada"
            else:
                return Resultado
        else:
            cursor = conn.cursor()
            consulta = "SELECT [Codigo de Factura],Fecha,[Nombre del Producto],[Precio por Unidad],[Cantidad a Comprar] FROM Facturas WHERE [Fecha] >= dateadd (mm, -?, getdate());"
            cursor.execute(consulta, (dias))
            # Con fetchall traemos todas las filas
            Resultado = cursor.fetchall()
            if len(Resultado)<1:
                return "Nada"
            else:
                return Resultado
            
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

def modificarInventario(conn,nombreV,codigoV,nombre,marca,cantidad,precio):
    cursor = conn.cursor()
    consulta = "UPDATE Productos SET Nombre = ? ,Marca = ? ,[Cantidad Inicial] = ? ,[Precio por unidad] = ? WHERE Codigo = ? AND Nombre = ?;" 
    cursor.execute(consulta,(nombre,marca,cantidad,precio,codigoV,nombreV))
    cursor.commit()
    
def eliminarProducto(conn,codigo,nombre):
    cursor = conn.cursor()
    consulta = "DELETE FROM Productos WHERE Codigo = ? AND Nombre = ?;" 
    cursor.execute(consulta,(codigo,nombre))
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

def consultaProductsModifyInventory(conn,name,codigo):
    try:
            cursor = conn.cursor()
            consulta = "SET NOCOUNT ON SELECT Nombre,Codigo,Marca,[Cantidad Inicial],[Precio por unidad] FROM Productos WHERE Codigo = ? AND Nombre = ?;"
            cursor.execute(consulta,(name,codigo))
            Resultado = cursor.fetchall()
            return Resultado
        
    except Exception as e:
        print("Ocurrió un error al consultar con where: ", e)
        

def consultaRegistrarProducto(conn,name,marca,quantity,price):
    try:
            cursor = conn.cursor()
            consulta = "set ANSI_WARNINGS off INSERT INTO Productos(Nombre,Marca,[Cantidad Inicial],[Precio por unidad])VALUES(?,?,?,?);"
            nombre = name
            marc = marca
            cantidad = quantity
            precio = price
            cursor.execute(consulta,(nombre,marc,cantidad,precio))
            cursor.commit()
                
    except Exception as e:
        print("Ocurrió un error al insertar: ", e)

def consultar_productos_stock(conn, cantidad_minima):
    try:
            cursor = conn.cursor()
            consulta = f"SET NOCOUNT ON SELECT Codigo, Nombre, Marca, [Cantidad Inicial] FROM Productos WHERE [Cantidad Inicial] <= ?;"
            cursor.execute(consulta,(cantidad_minima))
            Resultado = cursor.fetchall()
            return Resultado
        
    except Exception as e:
        print("Ocurrió un error al consultar con where: ", e)

        
# Cierre de conexión
def close():
    conn.close()
