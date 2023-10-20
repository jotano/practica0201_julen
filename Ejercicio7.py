correo_electronico = input("Introduce tu correo electrónico:")
nombre_usuario, dominio = correo_electronico.split("@")
correo_modificado = nombre_usuario + "@ceu.es"
print("Éste es otro correo electrónico con el mismo nombre:", correo_modificado)
input("Pulsa enter para salir")
