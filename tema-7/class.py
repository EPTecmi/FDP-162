import pdb
multiplicador = 1

numero = int(input("Ingresa un numero para darte la tabla de multiplicacion: "))
breakpoint()
while multiplicador <= 10:
    resultado = numero * multiplicador
    print(multiplicador,"X",numero,"=",resultado)
    multiplicador += 1
