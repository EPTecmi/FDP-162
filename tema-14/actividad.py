inventario = {
    "leche": 10,
    "tortillas": 20,
    "pan": 15
}

def mostrar_inventario(inventario):
    for producto, cantidad in inventario.items():
        print(producto,cantidad,sep=": ")

def agregar_producto(inventario):
    producto = input("Ingresa el producto")
    cantidad = int(input("Ingresa la cantidad"))
    inventario[producto] = cantidad

def actualizar_cantidad(inventario):
    producto = input("que producto quieres actualizar: ")
    cantidad = int(input("ingresa la nueva cantidad: "))
    inventario[producto] = cantidad

def eliminar_producto(inventario):
    producto = input("que producto quieres eliminar")
    del inventario[producto]


while True:
    print("1. Mostrar inventario")
    print("2. Agregar producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar producto")
    print("5. Salir")

    op = input("opcion: ")

    if op == "1":
        mostrar_inventario(inventario)
    elif op == "2":
        agregar_producto(inventario)
    elif op == "3":
        actualizar_cantidad(inventario)
    elif op == "4":
        eliminar_producto(inventario)
    elif op == "5":
        print("Salir")
        break
print("fin del programa")