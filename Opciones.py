import json
def Opciones(información):
    while True:
        
            print(f"\nHola {información[1]}, estas son las opciones disponibles: \n1. Eliminar empresa \n2. Modificar empresa, usuario u contraseña \n3. Volver al menú principal")
            OpciónElegida = int(input("¿Qué deseas hacer?: "))
            if OpciónElegida == 1: 
                Opción1(información)
            elif OpciónElegida == 2: 
                Opción2(información)
            elif OpciónElegida == 3: 
                print("Hasta pronto."); 
                break
            else: 
                raise Exception
        
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
            while not información[0].isalnum() or información[0].isnumeric():
                información[0] = input("Por favor, ingresa una empresa válida: ")
            print("Se ha cambiado el nombre de la empresa.")
        if PreguntaDeDato == "2":
            información[1] = input("Por favor, ingresa el nuevo nombre de usuario: ")
            while not información[1].isalpha:
                información[1] = input("Por favor, ingresa un usuario válido: ")
            print("Se ha cambiado el nombre de usuario.")
        if PreguntaDeDato == "3":
            información[2] = input("Por favor, ingresa la nueva contraseña: ")
            print("Se ha cambiado la contraseña.")
        if PreguntaDeDato == "4": return ""