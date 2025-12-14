from colorama import Fore, Style

from backend.services import productos_service
from frontend.ui.inputs import input_no_vacio, input_int, input_float, pausar
from frontend.ui.render import imprimir_tabla


def registrar_producto():
    print(Fore.CYAN + "\n=== Registrar producto ===" + Style.RESET_ALL)

    nombre = input_no_vacio("Nombre: ")
    descripcion = input("Descripción (opcional): ").strip()
    cantidad = input_int("Cantidad (>= 0): ", min_val=0)
    precio = input_float("Precio (>= 0): ", min_val=0.0)
    categoria = input("Categoría (opcional): ").strip()

    try:
        new_id = productos_service.registrar(nombre, descripcion, cantidad, precio, categoria)
        print(Fore.GREEN + f"✔ Producto registrado con ID {new_id}." + Style.RESET_ALL)
    except ValueError as e:
        print(Fore.RED + f"✖ Error: {e}" + Style.RESET_ALL)

    pausar()


def ver_productos():
    print(Fore.CYAN + "\n=== Listado de productos ===" + Style.RESET_ALL)
    imprimir_tabla(productos_service.listar())
    pausar()


def buscar_por_id():
    print(Fore.CYAN + "\n=== Buscar por ID ===" + Style.RESET_ALL)

    prod_id = input_int("Ingrese ID: ", min_val=1)
    row = productos_service.buscar_por_id(prod_id)

    if row:
        imprimir_tabla([row])
    else:
        print(Fore.YELLOW + "No se encontró un producto con ese ID." + Style.RESET_ALL)

    pausar()


def actualizar_por_id():
    print(Fore.CYAN + "\n=== Actualizar por ID ===" + Style.RESET_ALL)

    prod_id = input_int("Ingrese ID: ", min_val=1)
    existente = productos_service.buscar_por_id(prod_id)

    if not existente:
        print(Fore.YELLOW + "No existe un producto con ese ID." + Style.RESET_ALL)
        pausar()
        return

    print(Fore.MAGENTA + "Producto actual:" + Style.RESET_ALL)
    imprimir_tabla([existente])

    nombre = input_no_vacio("Nuevo nombre: ")
    descripcion = input("Nueva descripción (opcional): ").strip()
    cantidad = input_int("Nueva cantidad (>= 0): ", min_val=0)
    precio = input_float("Nuevo precio (>= 0): ", min_val=0.0)
    categoria = input("Nueva categoría (opcional): ").strip()

    try:
        n = productos_service.actualizar(prod_id, nombre, descripcion, cantidad, precio, categoria)
        if n:
            print(Fore.GREEN + "✔ Producto actualizado." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "No se pudo actualizar." + Style.RESET_ALL)
    except ValueError as e:
        print(Fore.RED + f"✖ Error: {e}" + Style.RESET_ALL)

    pausar()


def eliminar_por_id():
    print(Fore.CYAN + "\n=== Eliminar por ID ===" + Style.RESET_ALL)

    prod_id = input_int("Ingrese ID: ", min_val=1)
    existente = productos_service.buscar_por_id(prod_id)

    if not existente:
        print(Fore.YELLOW + "No existe un producto con ese ID." + Style.RESET_ALL)
        pausar()
        return

    print(Fore.MAGENTA + "Producto a eliminar:" + Style.RESET_ALL)
    imprimir_tabla([existente])

    conf = input(Fore.YELLOW + "Confirmar eliminación (s/n): " + Style.RESET_ALL).strip().lower()
    if conf == "s":
        n = productos_service.eliminar(prod_id)
        if n:
            print(Fore.GREEN + "✔ Producto eliminado." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "No se pudo eliminar." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "Operación cancelada." + Style.RESET_ALL)

    pausar()


def buscar_por_texto():
    print(Fore.CYAN + "\n=== Búsqueda por nombre o categoría ===" + Style.RESET_ALL)

    texto = input_no_vacio("Ingrese texto a buscar: ")
    resultados = productos_service.buscar_por_texto(texto)

    imprimir_tabla(resultados)
    pausar()


def reporte_stock_bajo():
    print(Fore.CYAN + "\n=== Reporte: stock bajo ===" + Style.RESET_ALL)

    limite = input_int("Ingrese límite (>= 0): ", min_val=0)

    try:
        imprimir_tabla(productos_service.reporte_stock_bajo(limite))
    except ValueError as e:
        print(Fore.RED + f"✖ Error: {e}" + Style.RESET_ALL)

    pausar()
