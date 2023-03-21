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
