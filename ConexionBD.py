import pyodbc

# Ejecución de consulta
def consultaLogin(user,contrasenia):
    server = 'LAPTOP-N9RBF9JA\KEVIN1'
    database = 'LibreriaUniverso'
    username = 'sa'
    password = '12345sa'
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    try:
            cursor = conn.cursor()
            consulta = "SELECT * FROM Usuarios WHERE Usuario = ? and Password = ?;"
            print(user)
            print(contrasenia)
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


# Cierre de conexión
def close():
    conn.close()
