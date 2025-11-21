import funciones as fn
import csv

def main():
    ventas = []
    archivo = input("Ingrese el nombre del archivo de ventas: ")
    ventas = fn.leer_archivo(archivo,ventas)

    while True: 
        opn = fn.menu()

        if opn == "1":
            ventas = fn.registrar_venta(ventas, archivo)
        elif opn == "2":
            fn.mostrar_ventas(ventas)
        elif opn == "3":
            fn.calcular_total(ventas)
        elif opn == "4":
            ventas = fn.eliminar_venta(ventas,archivo)
        elif opn == "5":
            print("Adios")
            break

if __name__ == "__main__":
    main()