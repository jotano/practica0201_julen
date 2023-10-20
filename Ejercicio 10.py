cesta_compra = input("Introduce los productos de tu cesta de compra separados por comas:")
lista_productos = cesta_compra.split(',')
print (*lista_productos, sep="\n")
input("Pulsa enter para salir")