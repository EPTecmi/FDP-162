# # Estructura básica
# contador = 1
# while contador <= 5:
#     print("Numero:", contador)
#     contador = contador + 1
# opcion = ""


## Menú de opciones con while
# while opcion != "0":
# while True:
#     print("menu")
#     print("1. primera opcion")
#     print("2. segunda opcion")
#     print("3. tercera opcion")
#     print("4. cuarta opcion")
#     print("5. quinta opcion")
#     print("0. Salir")
#     opcion = input("\ndame una opcion: ")

#     if opcion == "1":
#         print("\nelegiste la primer opcion")
#     elif opcion == "2":
#         print("\nelegiste la segunda opcion")
#     elif opcion == "3":
#         print("\nelegiste la tercera opcion")
#     elif opcion == "4":
#         print("\nelegiste la cuarta opcion")
#     elif opcion == "5":
#         print("\nelegiste la quinta opcion")
#     elif opcion == "0":
#         print("\nGracias por usar el programa")
#         break
#     else:
#         print("esa opcion no es válida")


# print("programa terminado")



import random

tiros = 1
while True:
    dado = random.randint(1,6)
    print("Tiro", tiros,":",dado)
    if dado == 6:
        print("Juego terminado")
        break
    tiros += 1