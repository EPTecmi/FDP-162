# archivo = open("datos.txt","w")
# with open("datos.txt","a") as archivo:
#     archivo.write("Hola Tecmilenio\n")
#     archivo.write("Estamos escribiendo un archivo\n")
#     archivo.write("Este es un texto nuevo")


# materias = ["Matematicas", "Fisica", "Programacion"]
# with open("materias.txt","w") as f:
#     for materia in materias:
#         f.write(materia+"\n")

import csv

with open("datos.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nombre", "Edad"])
    writer.writerow(["Jose", 20])
    writer.writerow(["Maria", 22])
    writer.writerow(["Juan", 18])
