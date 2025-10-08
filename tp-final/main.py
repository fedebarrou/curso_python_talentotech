# ================================
# Sistema de Gestión Básica de Productos
# Cada producto es [nombre, categoria, precioEntero]
# ================================

productos = []  # lista global de sublistas (cada ítem: [nombre, categoria, precio])

# ---------- Helpers de validación ----------
def leer_texto_no_vacio(prompt):
    # Pido texto hasta que el usuario ingrese algo no vacío
    while True:
        s = input(prompt).strip()  # elimino espacios al inicio/fin
        if s:
            return s
        print("⚠️  No puede estar vacío.")

def leer_entero_positivo(prompt):
    # Pido un número entero >= 0 (sin centavos)
    while True:
        s = input(prompt).strip()
        if s.isdigit():           # solo dígitos (evito letras, signos, puntos)
            n = int(s)
            if n >= 0:
                return n
        print("⚠️  Debe ser un número entero (sin centavos) y no negativo.")

def presione_para_continuar():
    # Pequeña pausa para que se lea la salida antes de volver al menú
    input("\nPresione Enter para continuar...")

# ---------- Operaciones ----------
def agregar_producto():
    print("\n=== Agregar producto ===")
    # Reutilizo validadores para evitar datos basura
    nombre = leer_texto_no_vacio("Nombre: ")
    categoria = leer_texto_no_vacio("Categoría: ")
    precio = leer_entero_positivo("Precio (entero, sin centavos): ")

    # Guardo el producto como sublista en la lista principal
    productos.append([nombre, categoria, precio])
    print("✅ Producto agregado correctamente.")

def mostrar_productos():
    print("\n=== Productos registrados ===")
    if not productos:
        # No hay nada que mostrar
        print("No hay productos cargados.")
        return

    # Recorro y muestro numerados (start=1)
    for i, p in enumerate(productos, start=1):
        nombre, categoria, precio = p
        print(f"{i}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")

    # También muestro el total registrados
    print(f"\nTotal de productos: {len(productos)}")

def buscar_producto():
    print("\n=== Buscar producto ===")
    if not productos:
        print("No hay productos cargados para buscar.")
        return

    # Convierto la búsqueda a minúsculas para hacerla case-insensitive
    q = leer_texto_no_vacio("Ingrese nombre a buscar: ").lower()
    encontrados = []

    # Coincidencia por subcadena dentro del nombre
    for i, p in enumerate(productos, start=1):
        if q in p[0].lower():
            encontrados.append((i, p))  # guardo el índice mostrado y la sublista

    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} coincidencia(s):")
        for idx, p in encontrados:
            nombre, categoria, precio = p
            print(f"{idx}. Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
    else:
        print("No se encontraron resultados.")

def eliminar_producto():
    print("\n=== Eliminar producto ===")
    if not productos:
        print("No hay productos registrados para eliminar.")
        return

    # Muestro primero para que el usuario vea el número
    mostrar_productos()
    pos = leer_entero_positivo("\nIngrese el número del producto a eliminar: ")

    # Valido que la posición exista en la lista
    if 1 <= pos <= len(productos):
        eliminado = productos.pop(pos - 1)  # -1 porque la lista es 0-based
        print(f"🗑️  Se eliminó: {eliminado[0]} (Categoría: {eliminado[1]}, Precio: ${eliminado[2]})")
    else:
        print("⚠️  Número fuera de rango.")

# ---------- Menú principal ----------
def menu():
    while True:
        # Menú textual simple, el programa corre hasta elegir 5 (Salir)
        print(
            "\nSistema de Gestión Básica De Productos\n"
            "1. Agregar producto\n"
            "2. Mostrar productos\n"
            "3. Buscar producto\n"
            "4. Eliminar producto\n"
            "5. Salir"
        )
        opcion = input("> ").strip()

        # Manejo de opciones con condicionales
        if opcion == "1":
            agregar_producto()
            presione_para_continuar()
        elif opcion == "2":
            mostrar_productos()
            presione_para_continuar()
        elif opcion == "3":
            buscar_producto()
            presione_para_continuar()
        elif opcion == "4":
            eliminar_producto()
            presione_para_continuar()
        elif opcion == "5":
            print("Gracias por utilizar el sistema. ¡Hasta luego!")
            break  # salgo del while True
        else:
            print("⚠️  Opción no válida. Intente nuevamente.")

# ---------- Ejecutar ----------
if __name__ == "__main__":
    # Solo ejecuto el menú si corro este archivo directamente
    menu()
