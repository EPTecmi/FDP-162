# from functions import leer_ventas, mostrar_totales,mostrar_ventas, formatear_monto, totales_por_cliente, consultar_cliente

import functions as f


def main():
	ventas = f.leer_ventas()
	if not ventas:
		return

	f.mostrar_ventas(ventas)
	totales = f.totales_por_cliente(ventas)
	f.mostrar_totales(totales)

	total_general = sum(totales.values())
	print(f"\nTotal general de ventas: {f.formatear_monto(total_general)}")

	nombre = input("\nIngrese el nombre del cliente a consultar: ")
	f.consultar_cliente(ventas, nombre)


if __name__ == "__main__":
	main()

