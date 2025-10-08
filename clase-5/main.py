# ==========================================
#Registrar los ingresos mensuales de un cliente durante 6 meses usando un bucle while para solicitar el ingreso de cada mes. Validar que los ingresos sean números positivos. Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

#Calcular el total acumulado durante los 6 meses y el promedio mensual. Mostrá este resultado al final del programa.
# ==========================================


#Funcion par obtener el ingreso mensual : dentro del try

def ingresar_monto (monto_ingresado):

  while True:
      s = input(monto_ingresado).strip().replace(",", ".")
      try:
          monto_validado = float(s)          # <-- puede lanzar ValueError
          if monto_validado < 0:
              print("⚠️  Valor no válido: el ingreso no puede ser negativo. Intente nuevamente.")
              continue                        # vuelve al inicio del while
          return monto_validado               # dato correcto: salgo de la función
      except ValueError:
          print("⚠️  Entrada inválida: ingrese solo números. Ejemplo: 1234.56")




def main():
    print("=== Registro de ingresos mensuales (6 meses) ===")
    
    #Array de ingresos
    ingresos = []
    mes = 1

    # Bucle while para 6 meses
    while mes <= 6:
        monto = ingresar_monto(f"Ingreso del mes {mes}: ")
        ingresos.append(monto)
        mes += 1

    # Cálculos
    total = sum(ingresos)
    promedio = total / 6

    # Resultados
    print("\n=== Resumen ===")

    # enumerate(ingresos, start=1) recorre la lista ingresos y te da: 
    #i: el número de mes empezando en 1 (1, 2, 3…).
    #val: el monto de ese mes.

    for i, val in enumerate(ingresos, start=1):
      print(f"Mes {i}: ${val:,.2f}")
      print(f"\nTotal acumulado (6 meses): ${total:,.2f}")
      print(f"Promedio mensual:          ${promedio:,.2f}")


#:,.2f es para darle formato decimal , de base estilo US


#Sirve para que solo se ejecute cuando el archivo se corre directamente y no cuando se importa desde otro módulo.
if __name__ == "__main__":
    main()