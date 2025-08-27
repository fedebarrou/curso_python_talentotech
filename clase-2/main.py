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



# INFO: el . en programacion sirve para acceder a los atributos y metodos de un elemento 

# \n es para hacer un salto de linea, sino aparece pegado al texto el input para escribir

# .strip es un metodo que limpia los espacios en blanco del principio y el final de una cadena ej: " Hola " -> "Hola"

# "f" en python se utiliza para interpolar, interpolar es poder poner en una cadena de texto una variable, hay muchas formas tambien esta concatenar que se usa el +  ej:

# print ("Hola, me llamo " + nombre + " y tengo " + " años") -> este es un ejemplo de concatenacion, pero es poco legible o facil equivocarse por lso espacios, tengo que poner los espacios en cada cadena de texto (lo que esta entre comillas, puede ser simple o dobles) 

# print(f"Hola, me llamo {nombre} y tengo {edad} años.") -> poniendo una f antes de usar un string (cadena de texto) puedo interpolar, en vez de usar los + pongo a las variables dentro de {}