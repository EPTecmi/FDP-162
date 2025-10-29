import pdb
print("=== Calculadora de factoriales y potencias ===")

opcion = 0
while opcion != 3:
    print("\nMenú:")
    print("1. Calcular factorial")
    print("2. Calcular potencia")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        n = int(input("Número: "))
        if n < 0:
            print("El factorial no está definido para negativos.")
        else:
            resultado = 1
            while n > 0:
                resultado *= n
                n -= 1
            print("Factorial:", resultado)

    elif opcion == 2:
        base = int(input("Base: "))
        exponente = int(input("Exponente: "))
        resultado = 1
        i = 0
        breakpoint()
        while i < exponente:
            resultado *= base
            i += 1
        print("Resultado:", resultado)

    elif opcion == 3:
        print("Adiós")
    else:
        print("Opción inválida")
