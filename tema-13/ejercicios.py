# materias = ("mate","fisica","fundamentos de programación", "ingles", "historia")

# print(materias[0])
# print(materias[-1])

# if "fundamentos de programacion" in materias:
#     print("Simon ese, si está")
# else:
#     print("nel carnal, no está")

matricula = input("Dame tu matricula: ")
nombre = input("Dame tu nombre: ")
edad = input("Dame tu edad: ")
carrera = input("Dame tu carrera: ")

alumno = (matricula, nombre, edad, carrera)

print(alumno)

for dato in alumno:
    print(dato)

# print("Matricula:",alumno[0])
# print("Nombre:",alumno[1])
# print("Edad:",alumno[2])
# print("Carrera:",alumno[3])