# matriz = [
#     [123,456,789],["hola","gente"],[True,False]
#     ]

# print(matriz)

#matriz = [[0 for j in range(3)] for i in range(3)]

matriz = [
    ["nombre","telefono","correo"],
    ["Edgar","1234567","sdjfk@jdls.com"],
    ["Jose","6141234567","joseelgrande28@gmail.com"]
]

for fila in matriz:
    for valor in fila:
        print(valor,end="\t")
    print()

# print(matriz)