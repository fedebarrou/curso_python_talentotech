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




#Hay distintos tipos de variables, int para numeros enteros, str para cadenas de texto , bool para booleanos (verdadero o falso) , float para numeros fraccionables

# En este caso -> edad = int(edad) 
# Vemos que uso int... pero si python no hace falta declarar el tipo de dato, es una diferencia con otros lenguajes... porque use int ? porque eso es un parseo, es convertir para asegurar que la variable que esta dentro de los () sea un numero entero, como es la edad


# .count es otro atributo que cuenta la cantidad de veces que aparece una cadena de texto que pidamos, en este caso fue @


# .title pone la primer letra de una cadena de texto en MAYUSCULA, capitaliza un texto


