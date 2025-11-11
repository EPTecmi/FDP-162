def menu():
    print("1. Registrar Contacto")
    print("2. Mostrar Contactos")
    print("3. Buscar Contacto")
    print("4. Salir")

    return input("Selecciona una opcion: ")

def plantilla_contacto(lista):
    if len(lista) != 0:
        print("Nombre", "Telefono", "Correo",sep="\t")
        for contacto in lista:
            print(contacto[0],contacto[1],contacto[2],sep="\t")
    else:
        print("No hay contactos")

def registrar_contacto(lista):
    nombre = input("Nombre: ")
    if buscar_contacto(nombre,lista) != False:
        print("Contacto ya existe")
        return lista

    telefono = input("Telefono: ")
    correo = input("Correo: ")

    nuevo_contacto = (nombre,telefono,correo)
    lista.append(nuevo_contacto)
    return lista

def mostrar_contactos(lista):
    plantilla_contacto(lista)


def buscar_contacto(nombre, lista):
    for contacto in lista:
        if nombre in contacto:
            return contacto
    return False

contactos = []
while True:
    op = menu()
    if op=="1":
        contactos = registrar_contacto(contactos)
    elif op=="3":
        nombre = input("nombre a buscar: ")
        contacto = buscar_contacto(nombre,contactos)
        if contacto != False:
            plantilla_contacto([contacto])
            continue
        print("Contacto no encontrado")
    elif op == "2":
        mostrar_contactos(contactos)
    elif op == "4":
        print("Adios")
        break

        