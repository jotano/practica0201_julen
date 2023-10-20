fecha_nacimiento = input("Escribe aquí tu fecha de nacimiento en formato dd/mm/aaaa:")
dia, mes, año = fecha_nacimiento.split("/")
if len(dia) == 1:
    dia = "0" + dia
if len(mes) == 1:
    mes = "0" + mes
print("Día:", dia)
print("Mes:", mes)
print("Año:", año)
input("Pulsa enter para salir")
