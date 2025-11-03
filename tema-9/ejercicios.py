lista_materias = ["mate","fisica","quimica","español","ingles"]

# print(lista_materias[0])
# print(lista_materias[-1])
# lista_nombres = []
# for i in range(5):
#     nombre = input("Dame nombre: ")
#     lista_nombres.append(nombre)
# print(lista_nombres)

# for i in range(4,-1,-1):
#     print(lista_nombres[i])

lista_temperaturas = [20.4,35.9,40.7,23.5,-2.5]
sum = 0
canti = 0
temp_max = -10000000
temp_min = 10000000
for temperatura in lista_temperaturas:
    sum += temperatura
    canti += 1

    if temperatura < temp_min:
        temp_min = temperatura
    if temperatura > temp_max:
        temp_max = temperatura

print("promedio temperaturas =", sum/canti)
print("Temperatura maxima:", temp_max)
print("Temperatura minima:", temp_min)


