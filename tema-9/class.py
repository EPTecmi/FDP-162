lista_compras = ["manzanas", "leche", "tortillas"]

lista_compras.append("pan")

lista_compras.insert(4,"peras")

for producto in lista_compras:
    print("Vas a comprar",producto)
    if producto == "leche":
        print("vas a traer 2 litros de", producto)


# print(lista_compras)