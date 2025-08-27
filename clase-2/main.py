nombre = input('Decime cual es tu nombre?\n').strip()
apellido =input('y tu apellido?\n').strip()
edad = input('cuantos años tenes?\n').strip()
correo_electronico = input ('dame tu email\n').strip()


# TARJETA
print("\n" + "="*40)
print("         TARJETA DE PRESENTACIÓN")
print("="*40)
print(f"Nombre completo : {nombre} {apellido}")
print(f"Edad            : {edad} años")
print(f"Correo          : {correo_electronico}")
print("="*40)