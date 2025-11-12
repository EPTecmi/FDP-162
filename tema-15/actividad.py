try:
    num1 = int(input("numero: "))
    num2 = int(input("numero: "))
    num3 = int(input("numero: "))
except ValueError:
    print("solo numeros")
else:
    lista = [num1,num2,num3]
    print(lista)
    print(sum(lista)/len(lista))
finally:
    print("Todo OK")

