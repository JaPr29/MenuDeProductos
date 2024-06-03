import json
def MostrarListado(información):
    try:
        with open("Productos.json", "r") as ImportarArchivo:
                    Productos = json.load(ImportarArchivo)
                    if Productos == []:
                        raise Exception
        print(f"\n Hola {información[1]}, aquí está la lista de los productos:\n")
        for Producto in Productos: # Muestra todos los productos guardados. // EN ESPERA DE CAMBIO (muy ineficiente para una lista de 1000 elementos por ej).
            print(f"Nombre: {Producto['Nombre']}  |  Precio: {Producto['Precio']}  |  Stock: {Producto['Stock']}  |  ID: {Producto['ID']}  |  Sección: {Producto['Sección']}")
        input("\nPresione enter para volver al menú.")

    except: # En caso de que no exista la lista de productos, se genera un error y muestra lo siguiente:
        print("No hay Productos guardados, debe agregar unos primero.")
        input("Presione enter para volver al menú.")

