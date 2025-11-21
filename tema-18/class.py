# archivo = open("materias.txt","r")
# # print(archivo.read())

# for linea in archivo:
#     if linea == "Matematicas\n":
#         print("si hay matematicas")
#     print(linea)

import csv

alumnos = []
with open("datos.csv","r") as file:
    reader = csv.DictReader(file)
    for fila in reader:
        alumnos.append(fila)

for alumno in alumnos:
    if alumno["Nombre"] == "Maria":
        alumno["Edad"] = 20

with open("datos.csv","w",newline="") as archivo:
    writer = csv.DictWriter(archivo, ["Nombre","Edad"])
    writer.writeheader()
    writer.writerows(alumnos)

