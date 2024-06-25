import json

def cargar_datos():
    with open('biblioteca.json', 'r') as archivo:
     return json.load(archivo)

def guardar_datos(data):
    with open('biblioteca.json', 'w') as archivo:
        json.dump(data, archivo, indent=4)

data = cargar_datos()

def agregar_usuario():
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el correo electrónico del usuario: ")
    fecha = input("Ingrese la fecha de registro (DD/MM/AAAA): ")

    nuevo_usuario = {
        "UsuarioID": len(data["UsuariosID"]) + 1,
        "Nombre": nombre,
        "Email": email,
        "FechaRegistro": fecha
    }

    data["Usuarios"].append(nuevo_usuario)
    guardar_datos(data)
    print("Usuario registrado exitosamente.")


def editar_usuario():
    usuario_id = int(input("Ingrese el ID del usuario que desea editar: "))
    encontrado = False

    for usuario in data["Usuario"]:
        if usuario["UsuarioID"] == usuario_id:
            encontrado = True
            print(f"Editando : {usuario['Nombre']}")
            nuevo_nombre = input(f"Nuevo nombre ({usuario['Nombre']}): ").strip() or usuario['Nombre']
            nuevo_email = input(f"Nuevo email ({usuario['Email']}): ").strip() or usuario['Email']
            nueva_fecha = input(f"Nueva fecha de registro ({usuario['FechaRegistro']}): ").strip() or usuario['FechaRegistro']

            usuario["Nombre"] = nuevo_nombre
            usuario["Email"] = nuevo_email
            usuario["FechaRegistro"] = nueva_fecha

            guardar_datos(data)
            print("Usuario editado exitosamente.")
            break

    if not encontrado:
        print("Usuario no encontrado.")


def eliminar_usuario():
    usuario_id = int(input("Ingrese el ID del usuario que desea eliminar: "))
    encontrado = False

    for usuario in data["Usuario"]:
        if usuario["UsuarioID"] == usuario_id:
            encontrado = True
            data["Usuario"].remove(usuario)
            guardar_datos(data)
            print("Usuario eliminado exitosamente.")
            break

    if not encontrado:
        print("Usuario no encontrado.")



def reporte():
    for Teatro in data ["Categoria"]:
        print (Teatro)
    for i, Cuento in data ["Categoria"]:
        print(Cuento, i)




while True:
    print("\n*** *** *** *** MENÚ PRINCIPAL *** *** *** ***")
    eleccion = int(input("Ingrese una opción:\n1) Mantenedor de usuarios\n2) Reportes\n3) Salir\n"))

    if eleccion == 1:
        while True:
            print("\n*** *** *** *** MANTENEDOR DE USUARIOS *** *** *** ***")
            eleccion2 = int(input("Ingrese una opción:\n1) Agregar usuario\n2) Editar usuario\n3) Eliminar usuario\n4) Buscar usuario\n5) Volver\n"))

            if eleccion2 == 1:
                agregar_usuario()
            elif eleccion2 == 2:
                editar_usuario()
            elif eleccion2 == 3:
                eliminar_usuario()
            elif eleccion2 == 4:
                print (data["Usuario"])
            elif eleccion2 == 5:
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    elif eleccion == 2:
        print("Entrando a reportes")
        reporte()

    elif eleccion==3:
        print("Buscando usuarios")
        print
    elif eleccion == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
