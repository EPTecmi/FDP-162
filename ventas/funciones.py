import csv
def menu():
    print("1. Registrar venta")
    print("2. Mostrar ventas")
    print("3. Calcular total")
    print("4. Eliminar venta")
    print("5. Salir")
    return input("Elige una opcion: ")

def leer_archivo(archivo, lista):
    try:
        with open("ventas/"+archivo+".csv","r",newline="") as file:
            reader = csv.DictReader(file)
            for fila in reader:
                lista.append(fila)
    except FileNotFoundError:
        with open("ventas/"+archivo+".csv","w", newline="") as file:
            lista = []
    return lista

def registrar_venta(ventas, archivo):
    try:
        producto = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        precio_unitario = float(input("Precio por unidad: "))

        ventas.append({"Producto":producto,"Cantidad":cantidad,"Precio Unitario":precio_unitario})
    except ValueError:
        print("Ese es un valor incorrecto\nVuelve a intentarlo")
        registrar_venta(ventas)
    
    escribir_archivo(ventas,archivo)
    
    print(ventas)
    return ventas

def escribir_archivo(ventas, archivo):
    try:
        with open("ventas/"+archivo+".csv","w",newline="") as file:
            writer = csv.DictWriter(file, ["Producto","Cantidad","Precio Unitario"])
            writer.writeheader()
            writer.writerows(ventas)
    except:
        pass

def mostrar_ventas(ventas):
    if len(ventas) < 1 :
        print("No hay ventas")
        return 
    
    print("Producto".center(20),"Cantidad".center(20),"Precio Unitario".center(20))
    for venta in ventas:
        precio_u = "$"+str(venta["Precio Unitario"])
        print(venta["Producto"].center(20),str(venta["Cantidad"]).center(20),precio_u.center(20))


def calcular_total(ventas):
    if len(ventas) < 1 :
        print("No hay ventas")
        return 
    suma = 0
    for venta in ventas:
        suma += int(venta["Cantidad"]) * float(venta["Precio Unitario"])
    print("Las ventas totales son:","$"+str(suma))
    pass

def eliminar_venta(ventas,archivo):
    if len(ventas) < 1 :
        print("No hay ventas")
        return 
    contador = 1
    print("ID".center(5),"Producto".center(20),"Cantidad".center(20),"Precio Unitario".center(20))
    for venta in ventas:
        precio_u = "$"+str(venta["Precio Unitario"])
        print(str(contador).center(5),venta["Producto"].center(20),str(venta["Cantidad"]).center(20),precio_u.center(20))
        contador += 1
    try:
        opcion = int(input("Elige un ID para eliminar"))
        del ventas[opcion-1]
        print("eliminado con exito")
    except ValueError:
        print("Valor de id invalido\nVuelve a intentarlo")
        eliminar_venta(ventas, archivo)
    except IndexError:
        print("ID No válido\n Intenta de nuevo")
        eliminar_venta(ventas,archivo)

    escribir_archivo(ventas, archivo)

    return ventas
    # ventas.pop(opcion-1)

    pass

def verificar_ventas(ventas):
    if len(ventas) < 1 :
        print("No hay ventas")
        return 