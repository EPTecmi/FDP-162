# try:
#     num = int(input("dame un numero: "))
#     print(10/num)
# except ValueError:
#     print("solo puedes usar numeros")
# except ZeroDivisionError:
#     print("no puedes dividir entre cero")
# else:
#     print("Operacion correcta/exitosa")
# finally:
#     print("el bloque try-except ha finalizado")

# print("programa terminado")

try:
    edad = int(input("cual es tu edad"))
    print()
except ValueError:
    print("error")