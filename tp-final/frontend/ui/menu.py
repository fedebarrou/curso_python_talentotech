from colorama import Fore, Style
from frontend.ui import controllers as c

def menu_principal():
    while True:
        print(Fore.CYAN + "\n=== Inventario - Menú Principal ===" + Style.RESET_ALL)

        print(Fore.YELLOW + "1)" + Style.RESET_ALL, "Registrar nuevo producto")
        print(Fore.YELLOW + "2)" + Style.RESET_ALL, "Visualizar productos")
        print(Fore.YELLOW + "3)" + Style.RESET_ALL, "Buscar producto por ID")
        print(Fore.YELLOW + "4)" + Style.RESET_ALL, "Actualizar producto por ID")
        print(Fore.YELLOW + "5)" + Style.RESET_ALL, "Eliminar producto por ID")
        print(Fore.YELLOW + "6)" + Style.RESET_ALL, "Búsqueda por nombre o categoría")
        print(Fore.YELLOW + "7)" + Style.RESET_ALL, "Reporte: stock bajo")
        print(Fore.RED + "0)" + Style.RESET_ALL, "Salir")

        op = input(Fore.GREEN + "Seleccione una opción: " + Style.RESET_ALL).strip()

        if op == "1":
            c.registrar_producto()
        elif op == "2":
            c.ver_productos()
        elif op == "3":
            c.buscar_por_id()
        elif op == "4":
            c.actualizar_por_id()
        elif op == "5":
            c.eliminar_por_id()
        elif op == "6":
            c.buscar_por_texto()
        elif op == "7":
            c.reporte_stock_bajo()
        elif op == "0":
            print(Fore.RED + "Saliendo..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción inválida." + Style.RESET_ALL)
