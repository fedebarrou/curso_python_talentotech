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




    # CONDICIONALES
    # 
    # if (nombre == "") significa "si nombre es igual a cadena de texto vacia" pasa lo que hay despues de los dos puntos
    # 
    # else seria "si no se cumple la condicion, va a suceder algo despues de los dos puntos"
    #
    # elif es una abreviatura en python, en otros lenguajes seria "if else" que basicamente seria "si no se cumplio la condicion anterior, que verifique si se cumple esta y pasa algo despues de los :"

    #OPERADORES
    #Hay muchos tipos de comparadores
  
    #Aritmeticos : 
    #print(a + b)   # 13  (suma)
    #print(a - b)   # 7   (resta)
    #print(a * b)   # 30  (multiplicación)
    #print(a / b)   # 3.333... (división flotante)
    #print(a // b)  # 3   (división entera)
    #print(a % b)   # 1   (módulo / resto)
    #print(a ** b)  # 1000 (potencia: 10^3)

    #Comparacion :
    #print(a == b)   # False (igualdad)
    #print(a != b)   # True  (distinto)
    #print(a > b)    # True
    #print(a < b)    # False
    #print(a >= b)   # True
    #print(a <= b)   # False

    #Logicos :
    #x = True
    #y = False

    #print(x and y)  # False - En otros lenguajes de programacion el and se usa con &&
    #print(x or y)   # True - En otros lenguajes de programacion el and se usa con ||
    #print(not x)    # False - En otros lenguajes de programacion el and se usa con !=
    #print("Python" in texto)  # True  - En otro lenguajes es incluedes o contains
    #print(x is y) #False - Esto en otros lenguajes se usa === que significa mismo valor y mismo tipo de dato, en este caso es el mismo tipo de dato "booleano" pero distinto valor, x es true , y es false
    


    #DATO
    # .isdigit() es otro metodo que sirve para constatar que la variable , en este caso edad sea un numero/digito







