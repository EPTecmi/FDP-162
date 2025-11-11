alumno = {"nombre":"Edgar","edad":25,"carrera":"TI","materias":{
    "Fundamentos de programacion": 90,
    "Ingles": 94
}}
alumno["nombre"] = "Jose"

# del alumno["edad"]
# print(alumno)
# for k in alumno:
#     print(k)
# for v in alumno.values():
#     print(v)
promedio = 0
for k,v in alumno.items():
    if k == "materias":
        suma = 0
        for valores in v.values():
            suma += valores
            promedio = suma / len(v)
            
alumno["promedio"] = promedio

print(alumno)
