import json
import Clases
import re
import Listar

try: # Importa la información de los productos y los pasa a una lista.
    with open("Productos.json", "r") as ImportarArchivoProductos:
        ProductosImportados = json.load(ImportarArchivoProductos)
        Productos = []
        for Producto in ProductosImportados:
            Productos.append(Clases.Producto(Producto["Nombre"], Producto["Precio"], Producto["Stock"], Producto["ID"], Producto["Sección"]))
except: # En caso de que no exista, crea la información.
    with open("Productos.json", "w") as CrearArchivo:
        Productos = []

def Agregar(ListaDeLaInformación): # Pide la lista de información para saber el usuario. // Es el menú de la función.
    while True:
        try:
            print(f"\nHola {ListaDeLaInformación[1]}, este es el menú para agregar un nuevo producto, dime ¿qué quieres hacer? \n1. Agregar un nuevo producto. \n2. Mostrar los productos actuales. \n3. Volver al menú principal.")
            OpciónElegida = int(input("Elige la opción que deseas hacer: "))
            if OpciónElegida == 1:
                AgregarProducto()
            elif OpciónElegida == 2:
                Listar.MostrarListado(ListaDeLaInformación)
            elif OpciónElegida == 3:
                break
            else:
                raise Exception
        except:
            print("Opción no valida. Intentalo de nuevo.")
    ProductosAGuardar = []
    for producto2 in Productos: # Pasa los productos de una lista a una lista de diccionarios para que pueda ser convertida a JSON.
        ProductosAGuardar.append({"Nombre": producto2.nombre, "Precio": producto2.precio, "Stock": producto2.stock, "ID": producto2.ID, "Sección": producto2.Sección})
    JSON = json.dumps(ProductosAGuardar, indent=4) # Convierte la lista de diccionarios a JSON.
    with open("Productos.json", "w") as GuardarProductos: # Guarda la lista.
        GuardarProductos.write(JSON)
    print("Se han guardado los datos.")

def AgregarProducto(): # Cuando se selecciona la opción de agregar un nuevo producto se inicia esta función, pide los datos y los añade a la lista.
    PatternNombre = re.compile(r"^[A-Z]{1}[a-z]+ [A-Z0-9]{1}[a-z0-9]+[a-z0-9]$|^[A-Z]{1}[a-z]+ [A-Z0-9]{1}[a-z0-9]+ [A-Z0-9]{1}[a-z0-9]+[a-z0-9]$|^[A-Z]{1}[a-z]+ [A-Z0-9]{1}[a-z0-9]+ [A-Z0-9]{1}[a-z0-9]+ [A-Z0-9]{1}[a-z0-9]+[a-z0-9]$")
    PatternPrecioStockId = re.compile(r'^[0-9]+$')
    PatternSección = re.compile(r"^[A-Z]{1}[a-z]+$|^[A-Z]{1}[a-z]+[ ]{1}[A-Z]{1}[a-z]+[a-z]$")
    while True:
        try:
            Nombre = input("Dime el nombre del nuevo producto: ")
            while not PatternNombre.search(Nombre):
                Nombre = input("Por favor, introduce un nombre válido: ")
            Precio = input("Dime el precio del nuevo producto: ")
            while not PatternPrecioStockId.search(Precio):
                Precio = input("Por favor, introduce un precio válido: ")
            Stock = input("Dime el stock del nuevo producto: ")
            while not PatternPrecioStockId.search(Stock):
                Stock = input("Por favor, introduce un stock válido: ")
            ID = input("Dime el ID del nuevo producto: ")
            while not PatternPrecioStockId.search(ID):
                ID = input("Por favor, introduce un ID válido: ")
            Sección = input("Dime la sección del nuevo producto: ")
            while not PatternSección.search(Sección):
                Sección = input("Por favor, introduce una sección válida: ")
            Productos.append(Clases.Producto(Nombre, Precio, Stock, f"#{ID}", Sección))
            print("El nuevo producto ha sido anadido a la lista exitosamente.\n")
            break
        except:
            "El dato ingresado es del tipo incorrecto. Intentalo de nuevo."

