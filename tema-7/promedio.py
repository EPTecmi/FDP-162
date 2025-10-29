import pdb
print("=== Sistema de Calificaciones ===")

n = int(input("Número de estudiantes: "))
suma = 0
i = 1
while i <= n:
    calificacion = int(input(f"Calificación del estudiante {i}: "))
    if calificacion < 0 or calificacion > 100:
        print("Error: calificación fuera de rango (0-100). Intente de nuevo.")
    else:
        suma += calificacion
        i += 1
breakpoint()
promedio = suma / (n 5)
print("Promedio del grupo:", promedio)

if promedio >= 70:
    print("Grupo aprobado")
else:
    print("Grupo reprobado")