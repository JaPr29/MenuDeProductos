import json
import time
import Agregar
import Listar
import Eliminar
import Editar
import Opciones
import Ayuda
import re
import sys
patternEmpresa = re.compile(r"[ ]{2}|^[ ]|[ ]$|[?'!@#$%^&*¡¿]+|^\d+$|^[a-z]") # El primero es para evitar multiples espacios, el segundo para evitar espacios al principio, el tercero para evitar al final, el cuarto para evitar caracteres extraños, el quinto para evitar que sea solo números.
patternUsuario = re.compile(r'^[A-Z]{1}[a-z]+[a-z]$|^[A-Z]{1}[a-z]+[ ]{1}[A-Z]{1}[a-z]+[a-z]$') # Permite poner nombre y apellido, pero solo si está especificado con mayúscula en cada inicio de palabra y solo dos palabras están disponibles.
patternContraseña = re.compile("[ ]+") # Evita que la contraseña pueda llevar espacios.
Contraseñaerrorcontador = 1

try: # Si la información existe, la importa y pasa directamente al menú.
    with open("información.json", "r") as ImportarArchivoInformación:
        información = json.load(ImportarArchivoInformación)        
        inicio = False
    print(f"¡Hola {información[1]}! Bienvenido al menú de productos de {información[0]}")
    if inicio == False: #Chequéa si es la primera vez que se inicia el programa.
        if información[2] != "":
            ContraseñaIngresada = input("Por favor, ingrese su contraseña: ")
            while ContraseñaIngresada != información[2]:
                print("\nContraseña incorrecta.")
                ContraseñaIngresada = input("Por favor, ingrese su contraseña: ")
                Contraseñaerrorcontador += 1
                if Contraseñaerrorcontador == 3:
                    print("\nIntentos agotados, espere 30 segundos para continuar.")
                    time.sleep(1)
                    Contraseñaerrorcontador = 1
                    OlvidoDeContraseña = input("¿Olvido su contraseña? \n 1. Si \n 2. No \n Elige una Opción: ")
                    if OlvidoDeContraseña == "1":
                        try:
                            with open("Seguridad.json", "r") as respuestas:
                                respuestas = json.load(respuestas)
                                Preguntas = ["¿Cuál es tu fecha de nacimiento?", "¿Cuál es tu familiar más cercano?", "¿Cuál es tu deporte favorito?"]
                                for i in range(3):
                                    respuesta = input(f"{Preguntas[i]}: ")
                                    if respuesta != respuestas[i]:
                                        print("Respuesta incorrecta. Saliendo de la sesión por seguridad.")
                                        time.sleep(2)
                                        sys.exit(0)
                        except SystemExit: sys.exit(0)                
                        except:
                            print("No se encontraron preguntas de seguridad. ¿Desea borrar los datos de la empresa? (No se borrarán los productos)")
                            BORRAR = input("1.Sí \n2.No: ")
                            if BORRAR == "1":
                                with open("información.json", "w") as BorrarInformación:
                                    BorrarInformación.write("")
                                    print("Se han borrado los datos de la empresa, cerrando sesión.")
                                    time.sleep(2)
                                    sys.exit(0)
                            elif BORRAR == "2":
                                print("Cerrando sesión. Para intentar nuevamente, reinicie el programa.")
                                time.sleep(2)
                                sys.exit(0)


                    if OlvidoDeContraseña == "2":
                        ContraseñaIngresada = input("Por favor, ingrese su contraseña:")

except SystemExit:
    sys.exit(0)
except: # En caso de que sea la primera vez que se inicia, crea la información.
    inicio = True
    CrearInformación = open("información.json", "w")
    información = []
    información.append(input("Bienvenido al menú de productos, por favor ingrese el nombre de su empresa: "))
    while información[0].strip() == "" or patternEmpresa.search(información[0]):
        información[0] = input("Por favor, ingrese una empresa válida.\nNo se aceptarán espacios innecesarios o caracteres especiales, ingrese el primer caracter en mayúsculas: ")
    información.append(input("Por favor, ingrese su usuario (Solo nombre y apellido o solo nombre): "))
    while not patternUsuario.search(información[1]):
        información[1] = input("Por favor, ingrese un usuario válido:\nNo se aceptarán espacios innecesarios, números o caracteres especiales: ")
    información.append(input("Por favor, ingrese su contraseña, en caso de no querer una, toque enter: "))
    while patternContraseña.search(información[2]):
        información[2] = input("Por favor, ingrese una contraseña válida (sin espacios): ")
    CrearInformación.write(json.dumps(información))
    CrearInformación.close
    PreguntaDeAyuda = input("Al ser la primera vez que ingresa, desea ver los conceptos básicos entrando al menú de ayuda? \n 1. Si \n 2. No \n Elige una Opción: ")
    if PreguntaDeAyuda == "1":
        Ayuda.Ayuda(información)
    elif PreguntaDeAyuda == "2":
        print("Abriendo menú")
        time.sleep(2)
    else:
        print("Opcion inválida, abriendo menú, si desea ayuda, ingrese al apartado de ayuda en el menú.")
        time.sleep(2)



while True: # Comienza el bucle del menú.
    try:
        print(f"\nEstas son las opciones disponibles: \n1. Agregar un nuevo producto \n2. Listar los Productos \n3. Eliminar un producto \n4. Editar información de un producto \n5. Opciones \n6. Ayuda \n7. Salir del menú")
        OpciónElegida = int(input("¿Qué deseas hacer?: "))
        if OpciónElegida == 1:
            Agregar.Agregar(información)
        elif OpciónElegida == 2:
            Listar.MostrarListado(información)
        elif OpciónElegida == 3:
            Eliminar.Eliminar(información)
        elif OpciónElegida == 4:
            Editar.Editar(información)
        elif OpciónElegida == 5:
            Opciones.Opciones(información)
        elif OpciónElegida == 6:
            Ayuda.Ayuda(información)
        elif OpciónElegida == 7:
            print(f"¡Adiós {información[1]}! :D") # La carita hace que la interfaz sea copada ;).
            time.sleep(1.5)
            break
        else: print("Opción no válida. Inténtalo de nuevo.")
    except:
        print("Opción no válida. Inténtalo de nuevo.")