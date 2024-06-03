import json
import re
patternEmpresa = re.compile("[?'!@#$%^&*¡¿]+")
patternUsuario = re.compile("[0-9?'!@#$%^&*¡¿]+")
patternContraseña = re.compile("[ ]+")

def Opciones(información):
    while True:
        
            print(f"\nHola {información[1]}, estas son las opciones disponibles: \n1. Eliminar empresa \n2. Modificar empresa, usuario u contraseña \n3. Crear preguntas de seguridad. \n4. Volver al menú principal")
            OpciónElegida = int(input("¿Qué deseas hacer?: "))
            if OpciónElegida == 1: 
                Opción1(información)
            elif OpciónElegida == 2: 
                Opción2(información)
            elif OpciónElegida == 3: 
                Opción3(información)
            elif OpciónElegida == 4: 
                print("Hasta pronto."); 
                break
            else: 
                print("Opcion inválida.")
        
    with open("información.json", "w") as GuardarInformación:
        GuardarInformación.write(json.dumps(información))


def Opción1(información):
    ChequeoDeSeguridad = input("Está seguro de querer eliminar los datos de la empresa y todos sus datos?\n 1. Si \n 2. No\n Elige una Opción: ")
    if ChequeoDeSeguridad == "1":
        with open("información.json", "w") as EliminarInformación:
            EliminarInformación.write(json.dumps([]))
    if ChequeoDeSeguridad == "2":
        print("No se realizaron cambios.")

def Opción2(información):
    while True:
        PreguntaDeDato = input("¿Qué dato deseas cambiar?: \n 1. Nombre de la empresa \n 2. Nombre de usuario \n 3. Contraseña \n 4. Volver al menú\n Elige una Opción: ")
        if PreguntaDeDato == "1":
            información[0] = input("Por favor, ingresa el nuevo nombre de la empresa: ")
            while información[0].strip() == "" or patternEmpresa.search(información[0]):
                información[0] = input("Por favor, ingresa una empresa válida: ")
            print("Se ha cambiado el nombre de la empresa.")
        if PreguntaDeDato == "2":
            información[1] = input("Por favor, ingresa el nuevo nombre de usuario: ")
            while información[1].strip() == "" or patternUsuario.search(información[1]):
                información[1] = input("Por favor, ingresa un usuario válido: ")
            print("Se ha cambiado el nombre de usuario.")
        if PreguntaDeDato == "3":
            información[2] = input("Por favor, ingresa la nueva contraseña: ")
            while patternContraseña.search(información[2]):
                información[2] = input("Por favor, ingresa una contraseña válida (sin espacios): ") 
            print("Se ha cambiado la contraseña.")
        if PreguntaDeDato == "4": return ""


def Opción3(información):
    Preguntas = ["¿Cuál es tu fecha de nacimiento?", "¿Cuál es tu familiar más cercano?", "¿Cuál es tu deporte favorito?"]
    OpciónElegida = input(f"Hola {información[1]}, a continuación se te dará tres preguntas que te serviran para recuperar tu cuenta \n en caso de que la pierdas por olvido de contraseña. \n ¿Estás de acuerdo? \n 1. Si \n 2. No \n Elige una Opción: ")
    if OpciónElegida == "1":
        with open("Seguridad.json", "w") as CrearPreguntas:
            Respuestas = []
            for i in range(3):
                Respuestas.append(input(f"Pregunta {i+1}: {Preguntas[i]} \n Respuesta: "))
            CrearPreguntas.write(json.dumps(Respuestas))
