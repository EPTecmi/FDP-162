nombre_archivo = input("dame un nombre para el archivo: ")

frase1=input("dame la frase1")
frase2=input("dame la frase2")
frase3=input("dame la frase3")

with open(nombre_archivo+".txt","w") as f:
    f.write(frase1)
    f.write("\n")
    f.write(frase2)
    f.write("\n")
    f.write(frase3)
    f.write("\n")