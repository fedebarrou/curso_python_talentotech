from typing import List, Tuple
ProductoRow = Tuple[int, str, str, int, float, str]

def imprimir_tabla(rows: List[ProductoRow]) -> None:
    if not rows:
        print("No hay resultados para mostrar.")
        return

    headers = ["ID", "Nombre", "Descripción", "Cantidad", "Precio", "Categoría"]
    widths = [len(h) for h in headers]

    for r in rows:
        widths[0] = max(widths[0], len(str(r[0])))
        widths[1] = max(widths[1], len(str(r[1] or "")))
        widths[2] = max(widths[2], len(str(r[2] or "")))
        widths[3] = max(widths[3], len(str(r[3])))
        widths[4] = max(widths[4], len(f"{r[4]:.2f}"))
        widths[5] = max(widths[5], len(str(r[5] or "")))

    def fmt(vals):
        return " | ".join(str(v).ljust(widths[i]) for i, v in enumerate(vals))

    line = "-" * (sum(widths) + 3 * (len(headers) - 1))
    print(line)
    print(fmt(headers))
    print(line)

    for r in rows:
        print(fmt([r[0], r[1] or "", r[2] or "", r[3], f"{r[4]:.2f}", r[5] or ""]))

    print(line)
