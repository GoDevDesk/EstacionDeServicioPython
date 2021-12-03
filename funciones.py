import sqlite3
import menus
from tabulate import tabulate

#ENLACE CON LA DB#
link = sqlite3.connect("estaciondeservicio.db")
cursorsql = link.cursor()


#FUNCION CLIENTES#
def nuevoCliente():
    print("-"*6,"Ingrese los datos del Cliente a continuación..","-"*6)
    clienteNombre = str(input("Ingrese el nombre y apellido: "))
    clienteCuit  = str(input("Ingrese el CUIT/CUIL: "))
    clienteDirec = str(input("Ingrese la dirección: "))
    clienteEmail = str(input("Ingrese la dirección de e-mail: "))

    sql_nuevo = "INSERT INTO clientes (cliente_id, cliente_nombre, cliente_cuit, cliente_direccion, cliente_email)  VALUES (?, ?, ?, ?, ?);"
    data_nuevo = (None, clienteNombre, clienteCuit, clienteDirec, clienteEmail)

    cursorsql.execute(sql_nuevo, data_nuevo,)
    link.commit()
    print("-"*33)    
    print("El cliente ha sido añadido de forma exitosa.")
    menus.Clientes()

def editarCliente():
    idAModificar = str(input("Seleccione el ID del cliente que quiere modificar: "))
    valorAModificar = str(input("Seleccione atributo que quiere modificar: "))
    valorModificado = str(input("Ingrese los datos correctos: "))
    
    sql_editar = str("UPDATE Clientes SET  "+valorAModificar+" = ? WHERE cliente_id = ?;")
    data_editar = (valorModificado, idAModificar)
    
    cursorsql.execute(sql_editar, data_editar,)
    link.commit()
    print("-"*33) 
    print("El cliente ha sido modificado correctamente.")
    menus.Clientes()

def consultarClientes():
    cursorsql.execute('SELECT * FROM Clientes;')    
    filas = cursorsql.fetchall()
    print(tabulate(filas, headers=['Cliente ID', 'Nombre', 'CUIT/CUIL', 'Dirección', 'E-mail']))
    link.commit()
    menus.Clientes()

def borrarCliente():
    campoBusqueda = input("Ingrese el campo donde buscar: ")
    datoCliente = str(input("Ingrese dato del campo del Cliente a eliminar: "))
    sqlBorrar = ("DELETE FROM Clientes WHERE "+campoBusqueda+" = '"+datoCliente+"';")

    cursorsql.execute(sqlBorrar)
    link.commit()
    print("-"*33)
    print("El cliente ha sido eliminado de la lista.")
    menus.Clientes()


#FUNCION PRODUCTOS#   
def nuevoProducto():
    print("-"*6,"Ingrese los detalles del Producto a continuación..","-"*6)
    productoID = str(input("Ingrese el ID de producto: "))
    productoDetalle  = str(input("Ingrese detalle del producto: "))
    productoLitros = int(input("Ingrese cantidad de litros a ingresar a stock: "))
    prodPrecioLitro = float(input("Ingrese el precio por litro del producto: "))

    sql_nuevo = "INSERT INTO Productos (producto_id, detalle, litros, precio_litro)  VALUES (?, ?, ?, ?);"
    prod_nuevo = (productoID, productoDetalle, productoLitros, prodPrecioLitro)
    cursorsql.execute(sql_nuevo, prod_nuevo,)
    link.commit()

    print("-"*33)    
    print("El producto ha sido añadido de forma exitosa.")
    menus.Productos()

def editarProducto():
    idAModificar = str(input("Seleccione el ID del producto que quiere modificar: "))
    valorAModificar = str(input("Seleccione atributo que quiere modificar: "))
    valorModificado = (input("Ingrese los datos correctos: "))
    
    sql_editar = str("UPDATE productos SET "+valorAModificar+" = ? WHERE producto_id = ?;")
    prod_editar = (valorModificado, idAModificar)    
    cursorsql.execute(sql_editar, prod_editar,)
    link.commit()
    print("-"*33)
    print("El producto ha sido modificado correctamente.")
    menus.Productos()

def consultarProductos():
    cursorsql.execute('SELECT * FROM Productos;')    
    filas = cursorsql.fetchall()
    
    print(tabulate(filas, headers=['Producto ID', 'Detalle', 'Litros en Stock', 'Precio por litro']))

    link.commit()
    menus.Productos()

def borrarProducto():
    campoBusqueda = input("Ingrese el campo donde buscar: ")
    datoProducto = input("Ingrese dato del campo del Producto a eliminar: ")
    
    sqlBorrar = ("DELETE FROM Productos WHERE "+campoBusqueda+" = "+datoProducto+";")

    cursorsql.execute(sqlBorrar)
    link.commit()
    print("-"*33)
    print("El producto ha sido eliminado de la lista.")
    menus.Productos()

#FUNCIONES CARGAS#
def nuevaCarga():
    print("-"*6,"Ingrese los datos de la carga a continuacion..","-"*6)
    cargaProductoId = str(input("Ingrese el ID del producto a cargar: "))
    cargaCantidadLitros = float(input("Ingrese la cantidad de litros: "))
    query = cursorsql.execute("SELECT precio_litro FROM Productos WHERE producto_id = '"+cargaProductoId+"';",).fetchone()
    cargaPrecioLitro = float(query[0])
    cargaTotal = float(cargaCantidadLitros*cargaPrecioLitro)

    sql_nuevo = "INSERT INTO cargas (carga_numero, producto_id, cant_litros, precio_litro, carga_total)  VALUES (?, ?, ?, ?, ?);"
    data_nuevo = (None, cargaProductoId, cargaCantidadLitros, cargaPrecioLitro, cargaTotal)

    cursorsql.execute(sql_nuevo, data_nuevo,)
    link.commit()
    print("-"*33)    
    print("La carga ha sido añadida de forma exitosa.")
    menus.Cargas()  


def editarCarga():
    idAModificar = str(input("Seleccione el numero de carga que quiere modificar: "))
    valorAModificar = str(input("Seleccione atributo que quiere modificar: "))
    valorModificado =  input("Ingrese los datos correctos: ")

    if valorAModificar == "precio_litro":
          exec1=str("UPDATE Cargas SET carga_total = cant_litros*"+str(valorModificado)+" where carga_numero="+idAModificar+";")           
          cursorsql.execute(exec1)
    
    if valorAModificar == "cant_litros":
          float(valorModificado)
          exec1=str("UPDATE Cargas SET carga_total = precio_litro*"+valorModificado+" where carga_numero="+idAModificar+";")           
          cursorsql.execute(exec1)
          
    
    sql_editar = str("UPDATE cargas SET "+valorAModificar+" = ? WHERE carga_numero = ?;")
    data_editar = (valorModificado, idAModificar) 

    cursorsql.execute(sql_editar, data_editar,)
    link.commit()
    print("-"*33)
    print("La carga ha sido modificado correctamente.")
    menus.Cargas()
    

def consultarCargas():
    cursorsql.execute('SELECT * FROM Cargas;')    
    filas = cursorsql.fetchall()
    print(tabulate(filas, headers=['Carga N°','Producto', 'Litros', 'Precio por litro', 'Total de Carga']))

    link.commit()
    menus.Cargas()

def borrarCarga():
    campoBusqueda = input("Ingrese el campo donde buscar: ")
    datoCliente = input("Ingrese dato del campo de la Carga a eliminar: ")
    
    sqlBorrar = ("DELETE FROM Cargas WHERE "+campoBusqueda+" = "+datoCliente+";")

    cursorsql.execute(sqlBorrar)
    link.commit()
    print("-"*33)
    print("La carga ha sido eliminada de la lista.")
    menus.Cargas()

#FACTURAS#    
def nuevaFactura():
    print("-"*6,"Ingrese a continuación los datos de la Factura..","-"*6)
    factura_fecha = str(input("Ingrese la fecha de factura (dd/mm/aaaa): "))
    clienteID  = int(input("Ingrese el ID de cliente: "))
    cargaNumero = int(input("Ingrese el N° de carga: "))
    query = cursorsql.execute('SELECT carga_total FROM Cargas WHERE carga_numero = '+str(cargaNumero)+';').fetchone()
    totalFactura = float(query[0])

    sql_nuevo = "INSERT INTO Facturas (factura_numero, factura_fecha, cliente_id, carga_numero, total_factura) VALUES (?, ?, ?, ?, ?);"
    data_nueva = (None, factura_fecha, clienteID, cargaNumero, totalFactura)
    

    cursorsql.execute(sql_nuevo, data_nueva,)
    link.commit()
    print("-"*33)
    print("La factura ha sido generada correctamente.")
    menus.Facturacion()

def editarFactura():
    idAModificar = int(input("Ingrese el N° de factura a modificar: "))
    valorAModificar = str(input("Seleccione atributo que quiere modificar: "))
    valorModificado = str(input("Ingrese los datos correctos: "))
    
    sql_editar = str('UPDATE Facturas SET '+valorAModificar+' = ? WHERE '+idAModificar+' = ?;')
    data_editar = (valorModificado, idAModificar)
    
    cursorsql.execute(sql_editar, data_editar,)
    link.commit()
    print("La factura ha sido modificada de forma exitosa.")
    menus.Facturacion()

def consultarFacturas():
    cursorsql.execute('SELECT * FROM Facturas;')
    filas = cursorsql.fetchall()    
    print(tabulate(filas, headers=['Factura N°', 'Fecha', 'Cliente ID', 'Carga N°', 'Total']))

    link.commit()
    menus.Facturacion()

def borrarFactura():
    campoBusqueda = input("Ingrese el campo donde buscar: ")
    datoCliente = input("Ingrese dato del campo de la factura a eliminar: ")
    
    sqlBorrar = ('DELETE FROM Facturas WHERE '+campoBusqueda+' = '+datoCliente+';')

    cursorsql.execute(sqlBorrar)
    link.commit()
    print("La factura ha sido eliminada de forma exitosa.")
    menus.Facturacion()