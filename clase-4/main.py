nombre = input('Decime cual es tu nombre?\n').strip()
apellido =input('y tu apellido?\n').strip()
edad = input('cuantos años tenes?\n').strip()
correo_electronico = input ('dame tu email\n').strip()

# Validaciones 
if not edad.isdigit():
    print("ERROR!")
    exit()

edad = int(edad)

if nombre == "" or apellido == "" or correo_electronico == "":
    print("ERROR!")
    exit()

nombre = nombre.title()
apellido = apellido.title()


if " " in correo_electronico or correo_electronico.count("@") != 1:
    print("ERROR!")
    exit()

# Clasificación por rango etario
if edad < 15:
    rango = "Niño/a"
elif 15 <= edad <= 18:
    rango = "Adolescente"
else:
    rango = "Adulto/a"

print("\n=== Datos del cliente ===")
print(f"Nombre    :\t{nombre}")
print(f"Apellido  :\t{apellido}")
print(f"Edad      :\t{edad} ({rango})")
print(f"Correo    :\t{correo_electronico}")
