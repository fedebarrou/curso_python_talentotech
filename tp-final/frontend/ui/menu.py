from frontend.ui import controllers as c

def menu_principal():
    while True:
        print("\n=== Inventario - Menú Principal ===")
        print("1) Registrar nuevo producto")
        print("2) Visualizar productos")
        print("3) Buscar producto por ID")
        print("4) Actualizar producto por ID")
        print("5) Eliminar producto por ID")
        print("6) Búsqueda por nombre o categoría (opcional)")
        print("7) Reporte: stock bajo (<= límite)")
        print("0) Salir")

        op = input("Seleccione una opción: ").strip()

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
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
