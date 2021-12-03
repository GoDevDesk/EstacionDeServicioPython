import funciones
import sqlite3
link = sqlite3.connect("estaciondeservicio.db")
cursorsql = link.cursor()

#MENU INICIO#
def menuInicio():
    print("[1] Menú Clientes")
    print("[2] Menú Productos")
    print("[3] Menú Cargas")
    print("[4] Menú Facturación")
    print("[0] Salir")

def elegirOpcion():
    print("-"*20)
    opcion = int(input("Elija una opción: "))
    print("-"*20)

    while opcion != 0:
        if opcion == 1:
            #opcion 1
            Clientes()
            break
        elif opcion == 2:
            #opcion 2
            Productos()
            break
        elif opcion == 3:
            #opcion 3
            Cargas()
            break
        elif opcion == 4:
            #opcion 3
            Facturacion()
            break
        else:
            print("Opción inválida!")
            print("-"*20)
            print("Bienvenido a la Estación de Servicio!")
            print("-"*20)
            menuInicio()
            print("-"*20)
            opcion = int(input("Elija una opción: "))

        print("-"*20)


#MENU CLIENTES#
def Clientes():

    def menuClientes():
        print("[1] Nuevo Cliente")
        print("[2] Editar Cliente")
        print("[3] Consultar Clientes")
        print("[4] Borrar Cliente")
        print("[5] Volver")
        print("[0] Salir")

    print("-"*20)
    print("Usted accedió al menu de Clientes")
    print("-"*20)
    menuClientes()
    print("-"*20)
    opcion = int(input("Elija una opción: "))
    print("-"*20)

    while opcion != 0:
        if opcion == 1:
            #opcion 1
            funciones.nuevoCliente()
            break
        elif opcion == 2:
            #opcion 2
            funciones.editarCliente()
            break
        elif opcion == 3:
            #opcion 3
            funciones.consultarClientes()
            break
        elif opcion == 4:
            #opcion 3
            funciones.borrarCliente()
            break
        elif opcion == 5:
            #opcion 0
            menuInicio()
            elegirOpcion()
            break
        else:
            print("Opción inválida!")
            print("-"*20)
            print("Usted accedió al menu de Clientes")
            print("-"*20)
            menuClientes()
            print("-"*20)
            opcion = int(input("Elija una opción: "))

        print("-"*20)


#MENU PRODUCTOS#
def Productos():

    def menuProductos():
        print("[1] Nuevo producto")
        print("[2] Editar producto")
        print("[3] Consultar productos")
        print("[4] Borrar producto")
        print("[5] Volver")
        print("[0] Salir")

    print("-"*20)
    print("Usted accedió al menu de Productos")
    print("-"*20)
    menuProductos()
    print("-"*20)
    opcion = int(input("Elija una opción: "))
    print("-"*20)

    while opcion != 0:
        if opcion == 1:
            #opcion 1
            funciones.nuevoProducto()
            break
        elif opcion == 2:
            #opcion 2
            funciones.editarProducto()
            break
        elif opcion == 3:
            #opcion 3
            funciones.consultarProductos()
            break
        elif opcion == 4:
            #opcion 3
            funciones.borrarProducto()
            break
        elif opcion == 5:
            #opcion 0
            menuInicio()
            elegirOpcion()
            break
        else:
            print("Opción inválida!")
            print("-"*20)
            print("Usted accedió al menu de Productos")
            print("-"*20)
            menuProductos()
            print("-"*20)
            opcion = int(input("Elija una opción: "))

        print("-"*20)

#MENU CARGAS#
def Cargas():
    def menuCargas():
        print("[1] Nueva carga")
        print("[2] Editar carga")
        print("[3] Consultar cargas")
        print("[4] Borrar carga")
        print("[5] Volver")
        print("[0] Salir")

    print("-"*20)
    print("Usted accedió al menu de Cargas")
    print("-"*20)
    menuCargas()
    print("-"*20)
    opcion = int(input("Elija una opción: "))
    print("-"*20)

    while opcion != 0:
        if opcion == 1:
            #opcion 1
            funciones.nuevaCarga()
            break
        elif opcion == 2:
            #opcion 2
            funciones.editarCarga()
            break
        elif opcion == 3:
            #opcion 3
            funciones.consultarCargas()
            break
        elif opcion == 4:
            #opcion 3
            funciones.borrarCarga()
            break
        elif opcion == 5:
            #opcion 0
            menuInicio()
            elegirOpcion()
            break
        else:
            print("Opción inválida!")
            print("-"*20)
            print("Usted accedió al menu de Clientes")
            print("-"*20)
            menuCargas()
            print("-"*20)
            opcion = int(input("Elija una opción: "))
        print("-"*20)

#MENU FACTURAS#
def Facturacion():

    def menuFacturas():
        print("[1] Nueva factura")
        print("[2] Editar factura")
        print("[3] Consultar facturas")
        print("[4] Borrar factura")
        print("[5] Volver")
        print("[0] Salir")

    print("-"*20)
    print("Usted accedió al menu de Facturas")
    print("-"*20)
    menuFacturas()
    print("-"*20)
    opcion = int(input("Elija una opción: "))
    print("-"*20)

    while opcion != 0:
        if opcion == 1:
            #opcion 1
            funciones.nuevaFactura()
            break
        elif opcion == 2:
            #opcion 2
            funciones.editarFactura()
            break
        elif opcion == 3:
            #opcion 3
            funciones.consultarFacturas()
            break
        elif opcion == 4:
            #opcion 3
            funciones.borrarFactura()
            break
        elif opcion == 5:
            #opcion 0
            menuInicio()
            elegirOpcion()
            break
        else:
            print("Opción inválida!")
            print("-"*20)
            print("Usted accedió al menu de Facturas")
            print("-"*20)
            menuFacturas()
            print("-"*20)
            opcion = int(input("Elija una opción: "))

        print("-"*20)