nombre = input('Decime cual es tu nombre?\n').strip()
apellido =input('y tu apellido?\n').strip()
edad = input('cuantos años tenes?\n').strip()
correo_electronico = input ('dame tu email\n').strip()

if (nombre == "" or apellido == "" or correo_electronico == "" or not edad.isdigit() or int(edad) <= 18):
    print("ERROR!")
else:
    # Datos en el orden que se ingresaron
    print(nombre)
    print(apellido)
    print(edad)
    print(correo_electronico)
