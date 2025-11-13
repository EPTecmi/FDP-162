# cadena = "Programa en Python"
# cadena = 'Programa en "Python"'
cadena = "Programa en \"Python\""
# print(type(cadena))
# print(cadena[0:8:3])

nombre = "           juan          "
apellido_paterno = "perez"
apellido_materno = "ERAZ"
email = "jose-perez@laempresatingona.com"

nombre_completo = nombre.upper().strip() + "-" + apellido_paterno + "-" + apellido_materno.lower()

# print(nombre_completo.title())
# print(nombre_completo.capitalize())
# print(nombre_completo.replace("eraz", "Dominguez"))

# print(nombre_completo.split("-"))
# print(email.split("@"))


def normalize(cadena):
    return cadena.strip().lower()

# print(normalize(input("dame tu nombre: ")))


print(f"Hola {normalize(nombre)}, con apellidos {normalize(apellido_paterno)} {normalize(apellido_materno)}")
resultado = 35/83
print(f"la division entre 35 y 83 es {resultado:.2f}")

