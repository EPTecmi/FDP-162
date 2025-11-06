def area_cuadrado(lado):
    return lado * lado

def area_rectangulo(base,altura):
    return base * altura

def area_circulo(radio):
    return 3.1416 * radio ** 2

def opciones_figuras():
    print("Elige una operacion (escribe 'salir' para terminar)")
    print("1. Area cuadrado")
    print("2. Area rectangulo")
    print("3. Area circulo")

    opcion = input("Opcion: ")

    if opcion == "1":
        lado = int(input("Dame un lado: "))
        figura = "Cuadrado"
        resultado = area_cuadrado(lado)
    elif opcion == "2":
        base = int(input("Dame la base: "))
        altura = int(input("Dame la altua: "))
        figura = "Rectangulo"
        resultado = area_rectangulo(base, altura)
    elif opcion == "3":
        radio= int(input("Dame el radio: "))
        figura = "Circulo"
        resultado = area_circulo(radio)
    elif opcion == "salir":
        return opcion
    else:
        print("opcion no valida")

    print("El Area del", figura, "es:",resultado)



while True:
   opcion = opciones_figuras()
   if opcion == "salir":
       break
    