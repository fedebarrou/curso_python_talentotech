# ==========================================
# Diccionario de productos {nombre: precio}
# - Agregar hasta escribir 'fin'
# - Validación de nombre y precio
# - Mostrar contenido tras cada operación
# ==========================================

def leer_nombre():
    while True:
        s = input("Nombre del producto (o 'fin' para terminar): ").strip()
        if s.lower() == "fin":
            return None
        if s == "":
            print("⚠️  El nombre no puede estar vacío.")
            continue
        return s

def leer_precio():
    while True:
        s = input("Precio (usar números; admite coma o punto): ").strip().replace(",", ".")
        try:
            p = float(s)
            if p < 0:
                print("⚠️  El precio no puede ser negativo.")
                continue
            return p
        except ValueError:
            print("⚠️  Entrada inválida. Ejemplos válidos: 100, 199.99, 2500")

def mostrar_diccionario(prod):
    if not prod:
        print("Diccionario vacío.")
        return
    print("Contenido actual:")
    # Mostrar ordenado por nombre del producto (case-insensitive)
    for nombre in sorted(prod.keys(), key=str.casefold):
        print(f"  - {nombre}: ${prod[nombre]:,.2f}")
    print()  # línea en blanco

def main():
    productos = {}

    print("=== Carga de productos (diccionario) ===")
    while True:
        nombre = leer_nombre()
        if nombre is None:   # 'fin'
            break
        precio = leer_precio()
        # Si el producto ya existe, se actualiza el precio
        productos[nombre] = precio
        print("✅ Operación realizada.")
        mostrar_diccionario(productos)

    print("\n=== Resultado final ===")
    mostrar_diccionario(productos)

if __name__ == "__main__":
    main()
