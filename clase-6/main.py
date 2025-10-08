

# Lista de clientes con errores
clientes = ["Ana", "Juan", "", "Marta", "  mArIa  ", "   ", "Fede"]

print("=== listado con validación ===")
for i, nombre in enumerate(clientes, start=1):
    nombre_validado = (nombre or "").strip()  # quita espacios y maneja None/""
    if nombre_validado == "":
        print(f"Cliente {i}: [ALERTA] Nombre no válido")
    else:
        print(f"Cliente {i}: {nombre_validado}")



print("\n=== listado con validación + Bonus ===")
for i, nombre in enumerate(clientes, start=1):
    nombre_validado = (nombre or "").strip()
    if nombre_validado == "":
        print(f"Cliente {i}: [ALERTA] Nombre no válido")
    else:
        # capitalize: primera letra mayúscula y resto minúscula
        print(f"Cliente {i}: {nombre_validado.capitalize()}")
