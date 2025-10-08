# ================================
# Carga y listado de clientes
# ================================

def leer_nombre():
    """Pide un nombre no vacío. Devuelve:
       - string del nombre válido
       - o None si el usuario escribió 'fin' (para terminar)
    """
    while True:
        s = input("Ingrese nombre de cliente (o 'fin' para terminar): ").strip()
        if s.lower() == "fin":
            return None
        if s == "":
            print("⚠️  Nombre vacío. Intente nuevamente.")
            continue
        return s

def main():
    clientes = []

    # Carga de nombres con validación y .append()
    while True:
        nombre = leer_nombre()
        if nombre is None:  # se escribió 'fin'
            break
        clientes.append(nombre)  # ← requisito: usar .append()

    # Ordenar alfabéticamente (case-insensitive)
    clientes.sort(key=str.casefold)

    # Mostrar lista ordenada
    print("\n=== Lista de clientes (ordenada) ===")
    for i, nombre in enumerate(clientes, start=1):
        print(f"Cliente {i}: {nombre}")

if __name__ == "__main__":
    main()
