def mostrar_menu():
    print("Elige una opcion")
    print("1. Agregar Contacto")
    print("2. Mostrar Contactos")
    print("3. Buscar Contacto")
    print("4. Salir")

def agregar_contacto(lista):
    nombre = input("Ingresa nombre: ")
    telefono = input("Ingresa telefono: ")
    correo = input("Ingresa correo: ")
    contacto = [nombre,telefono,correo]
    lista.append(contacto)
    print("Contacto agregado")

def mostrar_contactos(lista):
    print("Nombre|","Telefono|","Correo|",sep="\t")
    for contacto in lista:
        print(contacto[0]+"|",contacto[1]+"|",contacto[2]+"|",sep="\t")

def buscar_contacto(lista):
    nombre = input("Nombre de contacto a buscar: ")
    for contacto in lista:
        if nombre == contacto[0]:
            return contacto
    print("contacto no encontrado")
    
def salir():
    print("Adios amigo")

def imprimir_tabla(lista):
    print("Nombre|","Telefono|","Correo|",sep="\t")
    for contacto in lista:
        print(contacto[0]+"|",contacto[1]+"|",contacto[2]+"|",sep="\t")

lista=[]
while True:
    mostrar_menu()
    op=input("Opcion: ")

    if op=="1":
        agregar_contacto(lista)
    elif op=="2":
        imprimir_tabla(lista)
    elif op=="3":
        contacto = buscar_contacto(lista)
        if contacto is None:
            continue
        imprimir_tabla([contacto])
    elif op=="4":
        salir()
        break
    else:
        print("opcion no valida")
