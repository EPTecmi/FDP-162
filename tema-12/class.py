def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x,y):
    return x/y

resultado_suma = suma(5,3)

resultado_resta = resta(resultado_suma,2)

resultado_multiplicacion = multiplicacion(resultado_resta,5)

otra_multiplicacion= multiplicacion(resultado_multiplicacion,3)

# print(otra_multiplicacion)


def opciones(opcion):
    if opcion == 1:
        print("hola")
    elif opcion == 2:
        print("adios")
        return
    elif opcion == 3:
        print("otro hola")
    else:
        print("opcion invalida")
        
    print("este es el fin de mi funcion")


while True:
    opcion = int(input("opcion: "))
    opciones(opcion)