import csv


def formatear_monto(x):
	try:
		x = float(x)
	except Exception:
		return x
	if x.is_integer():
		return str(int(x))
	return f"{x:.2f}"


def leer_ventas():
	ventas = []
	paths_a_probar = ["ventas.csv", "tema-18/ventas.csv"]
	abierto = False
	for ruta in paths_a_probar:
		try:
			with open(ruta, encoding="utf-8", newline="") as f:
				lector = csv.DictReader(f)
				for r in lector:
					nombre = r.get("Nombre", "").strip()
					producto = r.get("Producto", "").strip()
					monto_raw = r.get("Monto", "0").strip()
					try:
						monto = float(monto_raw)
					except Exception:
						monto = 0.0
					ventas.append({"Nombre": nombre, "Producto": producto, "Monto": monto})
			abierto = True
			break
		except FileNotFoundError:
			continue
	if not abierto:
		print("No se encontró 'ventas.csv' en el directorio actual ni en 'tema-18/ventas.csv'.")
	return ventas


def mostrar_ventas(ventas):
	print("Ventas:")
	for v in ventas:
		print(f"Cliente: {v['Nombre']} - Producto: {v['Producto']} - Monto: {formatear_monto(v['Monto'])}")


def totales_por_cliente(ventas):
	totales = {}
	for v in ventas:
		nombre = v["Nombre"]
		totales[nombre] = totales.get(nombre, 0.0) + float(v["Monto"])
	return totales


def mostrar_totales(totales):
	print("\nTotal vendido por cliente:")
	for cliente, total in totales.items():
		print(f"{cliente}: {formatear_monto(total)}")


def consultar_cliente(ventas, nombre_buscar):
	nombre_buscar = nombre_buscar.strip()
	if not nombre_buscar:
		print("No se ingresó nombre.")
		return
	encontrados = [v for v in ventas if v["Nombre"].lower() == nombre_buscar.lower()]
	if not encontrados:
		print(f"El cliente '{nombre_buscar}' no existe en las ventas.")
		return
	print(f"\nCompras de {encontrados[0]['Nombre']}:")
	for v in encontrados:
		print(f"Producto: {v['Producto']} - Monto: {formatear_monto(v['Monto'])}")
	total = sum(float(v["Monto"]) for v in encontrados)
	print(f"Total acumulado de {encontrados[0]['Nombre']}: {formatear_monto(total)}")