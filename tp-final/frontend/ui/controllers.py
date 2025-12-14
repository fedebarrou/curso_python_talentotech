from backend.services import productos_service
from frontend.ui.inputs import input_no_vacio, input_int, input_float, pausar
from frontend.ui.render import imprimir_tabla

def registrar_producto():
    print("\n=== Registrar producto ===")
    nombre = input_no_vacio("Nombre: ")
    descripcion = input("Descripción (opcional): ").strip()
    cantidad = input_int("Cantidad (>= 0): ", min_val=0)
    precio = input_float("Precio (>= 0): ", min_val=0.0)
    categoria = input("Categoría (opcional): ").strip()

    try:
        new_id = productos_service.registrar(nombre, descripcion, cantidad, precio, categoria)
        print(f"Producto registrado con ID {new_id}.")
    except ValueError as e:
        print(f"Error: {e}")
    pausar()

def ver_productos():
    print("\n=== Listado de productos ===")
    imprimir_tabla(productos_service.listar())
    pausar()

def buscar_por_id():
    print("\n=== Buscar por ID ===")
    prod_id = input_int("Ingrese ID: ", min_val=1)
    row = productos_service.buscar_por_id(prod_id)
    if row:
        imprimir_tabla([row])
    else:
        print("No se encontró un producto con ese ID.")
    pausar()

def actualizar_por_id():
    print("\n=== Actualizar por ID ===")
    prod_id = input_int("Ingrese ID: ", min_val=1)
    existente = productos_service.buscar_por_id(prod_id)
    if not existente:
        print("No existe un producto con ese ID.")
        pausar()
        return

    print("Producto actual:")
    imprimir_tabla([existente])

    nombre = input_no_vacio("Nuevo nombre: ")
    descripcion = input("Nueva descripción (opcional): ").strip()
    cantidad = input_int("Nueva cantidad (>= 0): ", min_val=0)
    precio = input_float("Nuevo precio (>= 0): ", min_val=0.0)
    categoria = input("Nueva categoría (opcional): ").strip()

    try:
        n = productos_service.actualizar(prod_id, nombre, descripcion, cantidad, precio, categoria)
        print("Producto actualizado." if n else "No se pudo actualizar.")
    except ValueError as e:
        print(f"Error: {e}")
    pausar()

def eliminar_por_id():
    print("\n=== Eliminar por ID ===")
    prod_id = input_int("Ingrese ID: ", min_val=1)
    existente = productos_service.buscar_por_id(prod_id)
    if not existente:
        print("No existe un producto con ese ID.")
        pausar()
        return

    print("Producto a eliminar:")
    imprimir_tabla([existente])

    conf = input("Confirmar eliminación (s/n): ").strip().lower()
    if conf == "s":
        n = productos_service.eliminar(prod_id)
        print("Producto eliminado." if n else "No se pudo eliminar.")
    else:
        print("Operación cancelada.")
    pausar()

def buscar_por_texto():
    print("\n=== Búsqueda por nombre o categoría ===")
    texto = input_no_vacio("Ingrese texto a buscar: ")
    imprimir_tabla(productos_service.buscar_por_texto(texto))
    pausar()

def reporte_stock_bajo():
    print("\n=== Reporte: stock bajo ===")
    limite = input_int("Ingrese límite (>= 0): ", min_val=0)
    try:
        imprimir_tabla(productos_service.reporte_stock_bajo(limite))
    except ValueError as e:
        print(f"Error: {e}")
    pausar()
