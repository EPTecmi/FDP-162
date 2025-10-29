ANIO_ACTUAL = 2025

anio_nacimiento = int(input("Dame tu año de nacimiento"))

edad_actual = ANIO_ACTUAL - anio_nacimiento
edad_en_10 = edad_actual + 10

print("Tienes " + str(edad_actual) + " y en 10 años tendrás " + str(edad_en_10))