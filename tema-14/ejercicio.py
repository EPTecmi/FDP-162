alumnos = {
    "T1234560":{
        "nombre": "Edgar",
        "edad": 34,
        "carrera": "TI"
    },
    "T345345":{
        "nombre":"Jose",
        "edad":"27",
        "carrera":"negocios"
    },
    "T485739":{
        "nombre":"Maria",
        "edad": 23,
        "carrera":"diseño"
    }
}

alumnos["T5811684"] = {"nombre":"Ana","edad":19,"carrera":"empresas"}

for alumno in alumnos.values():
    print(alumno["nombre"])

print(alumnos)
alumnos["T345345"]["edad"] = 20
del alumnos["T1234560"]
print(alumnos)