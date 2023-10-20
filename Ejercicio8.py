precio = input("Cuanto vale el producto?(Euros con dos decimales)")
if "." in precio:
    euros, centimos = [int(x) for x in precio.split(".")]
    print("Euros:", euros)
    print("Céntimos:", centimos)
input("Pulsa enter para salir")
