def Ayuda(información):
    while True:
        OpciónElegida = input(f"\nHola {información[1]}, este es el menú de ayuda, te servirá para entender conceptos básicos sobre el programa, ya sea cómo agregar productos u otras cuestiones. \n ¿En qué necesitas ayuda? \n1. ¿Qué debo poner en cada espacio? / ¿Cómo agrego mis productos? \n2. ¿Cómo cambio mis datos? \n3. ¿Qué pasa si olvido mi contraseña? \n4. Volver al menú principal \n Elige una Opción: ")
        if OpciónElegida == "1":
            print("\nNombres permitidos: En el menú se aceptarán solo ciertos tipos de caracteres en cada espacio y, además, \nse pedirá que se ingresen las mayúsculas y minúsculas correspondientes. \nEl objetivo de esto es hacer que el menú sea legible, profesional y funcional, en cada menú se puede consultar el listado de los productos \npara que no sea dificil editarlos, eliminarlos, etcétera.\nPara agregar productos, entra al apartado de agregar en el menú principal y sigue las reglas previamente dichas. \n")
            MasAyuda = input("Necesitas una guía para saber qué poner en cada espacio? \n 1. Si \n 2. No \n Elige una Opción: ")
            if MasAyuda == "1":
                print("\n\t- En el espacio de nombre de empresa, se permitirán letras y números mientras que el nombre completo no consista de únicamente números. \n\t- En el espacio de nombre de usuario se permitirán dos palabras(Nombre y Apellido), siendo la segunda opcional, además, deberá estar señalado\n\t  cada inicio de palabra con una mayúscula y el resto con minúsculas. \n\t- En el espacio de nombre de producto se podrán poner desde dos (Nombre del producto y marca) hasta 4 palabras pero siguiendo las reglas anteriores. \n\t- En el espacio de precio, stock e id solo se aceptarán números. \n\t- En el espacio de sección, se aceptan múltiples palabras como pasaba en el espacio de productos. \n")
                input("Presione enter para volver al menú.")
            elif MasAyuda == "2":
                 print("Volviendo al menú.")
            else :
                print("Opción no válida, volviendo al menú.")
        elif OpciónElegida == "2":
                print('\nPara cambiar tus datos debes entrar al apartado "Opciones" en el menú principal y elegir la opcion 2, ahí tendrás todas las opciones para cambiar tus datos.')
                input("\nPresione enter para volver al menú.")
        elif OpciónElegida == "3":
                print('\nPara evitar perder tu cuenta debido al olvido de la contraseña, tienes que entrar al apartado de "Opciones" en el menú principal y elegir la opción 3, de\nesta manera, si olvidas tu contraseña podrás en su lugar responder unas preguntas de seguridad para recuperar tu cuenta.')
                input("\nPresione enter para volver al menú.")
        elif OpciónElegida == "4":
                print("¡Vuelve si necesitas ayuda!\n")
                break
        else:
            print("Opción no válida, inténtalo otra vez.")