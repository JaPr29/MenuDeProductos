import json
def Listar(ListaDeLaInformación): # Pide la lista de información para saber el usuario. // Es el menú de la función.
    try:
        with open("Productos.json", "r") as ImportarArchivo:
                    Productos = json.load(ImportarArchivo)
                    if Productos == []:
                        raise Exception
        while True: # Si existe la lista y no está vacía, se muestra el menú.
            try:
                print(f"\nHola {ListaDeLaInformación[1]}, este es el menú para ver los Productos, dime ¿Qué quieres hacer? \n1. Listar los Productos \n2. Volver al menú principal")
                OpciónElegida = int(input("Elige la opción que deseas hacer: "))
                if OpciónElegida == 1:
                    print()
                    for Producto in Productos: # Muestra todos los productos guardados. // EN ESPERA DE CAMBIO (muy ineficiente para una lista de 1000 elementos por ej).
                        print(f"Nombre: {Producto['Nombre']}, Precio: {Producto['Precio']}, Stock: {Producto['Stock']}, ID: {Producto['ID']}, Sección: {Producto['Sección']}")
                elif OpciónElegida == 2: 
                    break
                else: 
                    raise Exception
            except:
                print("Opción no valida. Intentalo de nuevo.")
    except: # En caso de que no exista la lista de productos, se genera un error y muestra lo siguiente:
        print("No hay Productos guardados, debe agregar unos primero.")
        input("Presione enter para volver al menú principal.")