import json
import Listar
import Clases

def Eliminar(información):	
    try: # Importa la información de los productos y los pasa a una lista.
        with open("Productos.json", "r") as ImportarArchivoProductos:
            ProductosImportados = json.load(ImportarArchivoProductos)
            if ProductosImportados == []:
                raise Exception
            Productos = []
            for Producto in ProductosImportados:
                Productos.append(Clases.Producto(Producto["Nombre"], Producto["Precio"], Producto["Stock"], Producto["ID"], Producto["Sección"]))
    except: 
        print("No hay Productos para eliminar.")
        input("Presione enter para volver al menú principal.")
    
    while True: # Si existe la lista y no está vacía, se muestra el menú.
        try:
            print(f"\nHola {información[1]}, este es el menú para eliminar un Producto, dime ¿Qué quieres hacer? \n1. Eliminar un Producto. \n2. Consultar listado. \n3. Volver al menú principal.")
            OpciónElegida = int(input("Elige la función que deseas hacer: "))
            if OpciónElegida == 1:
                EliminarProducto(Productos)
            elif OpciónElegida == 2:
                Listar.MostrarListado(información)
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
        

def EliminarProducto(Productos):
    while True:
        Buscar = input("Dime el nombre del producto que quieres eliminar: ")
        for producto in Productos:
            if Buscar == producto.nombre:
                print("Se ha encontrado el producto.")
                ChequeoDeSeguridad = input("Está seguro de querer eliminar el producto?\n 1. Si \n 2. No\n Elige una Opción: ")
                if ChequeoDeSeguridad == "1":
                    Productos.pop()
                    print("Se ha eliminado el producto exitosamente.")
                if ChequeoDeSeguridad == "2":
                    print("No se realizaron cambios.")
                return ""
        print("No se ha encontrado el producto.")