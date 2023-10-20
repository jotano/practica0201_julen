producto = input("Escribe el nombre del producto:")
precio = float(input("Escribe el precio del producto:"))
unidades = int(input("Escribe el número de unidades:"))
coste_total = precio * unidades
cadena= f'{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {coste_total:11.2f}€'
print(cadena)
input("Pulsa enter para salir")