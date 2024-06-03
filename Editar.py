import json
import Clases
import Listar
import re
def Editar(información):
    try:
        with open("Productos.json", "r") as ImportarArchivoProductos: # Pasa la información de los productos a una lista.
            ProductosImportados = json.load(ImportarArchivoProductos)
            Productos = []
            for Producto in ProductosImportados:
                Productos.append(Clases.Producto(Producto["Nombre"], Producto["Precio"], Producto["Stock"], Producto["ID"], Producto["Sección"]))
        while True: # Empieza el menú.
            try:
                print(f"Hola {información[1]}, este es el menú para editar los Productos, recuerda que para editar un producto debes poner su nombre de la manera correspondiente \n Puedes consultar el listado para ello.\n dime ¿Qué quieres hacer? \n1. Editar un Producto. \n2. Consultar listado. \n3. Volver al menú principal.")
                OpciónElegida = int(input("Elige la función que deseas hacer: "))
                if OpciónElegida == 1:
                    EditarProducto(Productos)
                elif OpciónElegida == 2:
                    Listar.MostrarListado(información)
                elif OpciónElegida == 3:
                    break
                else:
                    raise Exception
            except:
                print("Opción no valida. Intentalo de nuevo.")
    except:
        print("No hay Productos guardados, debe agregar unos primero.")
        input("Presione enter para volver al menú principal.")
    ProductosAGuardar = []
    for producto2 in Productos: # Pasa los productos de una lista a una lista de diccionarios para que pueda ser convertida a JSON.
        ProductosAGuardar.append({"Nombre": producto2.nombre, "Precio": producto2.precio, "Stock": producto2.stock, "ID": producto2.ID, "Sección": producto2.Sección})
    JSON = json.dumps(ProductosAGuardar, indent=4) # Convierte la lista de diccionarios a JSON.
    with open("Productos.json", "w") as GuardarProductos: # Guarda la lista.
        GuardarProductos.write(JSON)
    print("Se han guardado los datos.")
#################################################################################################
def EditarProducto(ListaDeProductos):
    PatternNombre = re.compile(r"^[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+[a-z]$|^[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+[a-z]$|^[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+[a-z]$")
    PatternPrecioStockId = re.compile(r'^[0-9]+$')
    PatternSección = re.compile(r"^[A-Z]{1}[a-z]+$|^[A-Z]{1}[a-z]+[ ]{1}[A-Z]{1}[a-z]+[a-z]$")
    while True:
        Buscar = input("Dime el nombre del producto que quieres editar: ")
        for producto in ListaDeProductos:
            if Buscar == (producto.nombre):
                print("Se ha encontrado el producto.")
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}, ID: {producto.ID}, Sección: {producto.Sección}")
                while True:
                    print("¿Qué quieres editar? \n1. Nombre \n2. Precio \n3. Stock \n4. ID \n5. Sección \n6. Volver")
                    OpciónElegida = int(input("Elige la función que deseas hacer: "))
                    if OpciónElegida == 1:
                        NuevoNombre = input("Dime el nuevo nombre: ")
                        while not PatternNombre.search(NuevoNombre):
                            NuevoNombre = input("Por favor, introduce un nombre válido: ")
                        producto.nombre = NuevoNombre
                        print("Se ha editado el nombre.")

                    elif OpciónElegida == 2:
                        NuevoPrecio = input("Dime el nuevo precio: ")
                        while not PatternPrecioStockId.search(NuevoPrecio):
                            NuevoPrecio = input("Por favor, introduce un precio válido: ")
                        producto.precio = NuevoPrecio
                        print("Se ha editado el precio.")

                    elif OpciónElegida == 3:
                        NuevoStock = input("Dime el nuevo stock: ")
                        while not PatternPrecioStockId.search(NuevoStock):
                            NuevoStock = input("Por favor, introduce un stock válido: ")
                        producto.stock = NuevoStock
                        print("Se ha editado el stock.")

                    elif OpciónElegida == 4:
                        NuevoID = input("Dime el nuevo ID: ")
                        while not PatternPrecioStockId.search(NuevoID):
                            NuevoID = input("Por favor, introduce un ID válido: ")
                        producto.ID = NuevoID
                        print("Se ha editado el ID.")

                    elif OpciónElegida == 5:
                        NuevaSección = input("Dime la nueva sección: ")
                        while not PatternSección.search(NuevaSección):
                            NuevaSección = input("Por favor, introduce una sección válida: ")
                        producto.Sección = NuevaSección
                        print("Se ha editado la sección.")

                    elif OpciónElegida == 6:
                        break
                    else:
                        print("Opción no valida. Intentalo de nuevo.")
                return
        print("No se ha encontrado el producto.")