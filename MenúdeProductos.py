import json
import Agregar
import Listar
import Eliminar
import Editar
import Opciones

try: # Si la información existe, la importa y pasa directamente al menú.
    with open("información.json", "r") as ImportarArchivoInformación:
        información = json.load(ImportarArchivoInformación)        
        inicio = False
except: # En caso de que sea la primera vez que se inicia, crea la información.
    inicio = True
    CrearInformación = open("información.json", "w")
    información = []
    información.append(input("Bienvenido al menú de productos, por favor ingrese el nombre de su empresa: "))
    while not información[0].isalnum() or información[0].isnumeric():
        información[0] = input("Por favor, ingrese una empresa válida: ")
    información.append(input("Por favor, ingrese su usuario: "))
    while not información[1].isalpha:
        información[1] = input("Por favor, ingrese un usuario válido: ")
    información.append(input("Por favor, ingrese su contraseña, en caso de no querer una, toque enter: "))
    CrearInformación.write(json.dumps(información))
    CrearInformación.close

print(f"¡Hola {información[1]}! Bienvenido al menú de productos de {información[0]}")
if inicio == False: #Chequéa si es la primera vez que se inicia el programa.
    if información[2] != "":
        Password = input("Por favor, ingrese su contraseña: ")
        while Password != información[2]:
            Password = input("Contraseña incorrecta: ")

while True: # Comienza el bucle del menú.
    try:
        print(f"\n Bien {información[1]}, estas son las opciones disponibles: \n1. Agregar un nuevo producto \n2. Listar los Productos \n3. Eliminar un producto \n4. Editar información de un producto \n5. Opciones \n6. Salir del menú")
        OpciónElegida = int(input("¿Qué deseas hacer?: "))
        if OpciónElegida == 1:
            print()
            Agregar.Agregar(información)
        elif OpciónElegida == 2:
            print()
            Listar.Listar()
        elif OpciónElegida == 3:
            print()
            Eliminar.Eliminar()
        elif OpciónElegida == 4:
            Editar.Editar()
        elif OpciónElegida == 5:
            Opciones.Opciones()
        elif OpciónElegida == 6:
            break
        else: print("Opción no válida. Inténtalo de nuevo.")
    except:
        print("Opción no válida. Inténtalo de nuevo.")