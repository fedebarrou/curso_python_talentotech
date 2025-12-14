from typing import Optional, List, Tuple
from backend.repositories import productos_repo

ProductoRow = Tuple[int, str, str, int, float, str]

def _validar(nombre: str, cantidad: int, precio: float) -> None:
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")

def registrar(nombre: str, descripcion: str, cantidad: int, precio: float, categoria: str) -> int:
    _validar(nombre, cantidad, precio)
    return productos_repo.crear(nombre.strip(), descripcion.strip(), cantidad, precio, categoria.strip())

def listar() -> List[ProductoRow]:
    return productos_repo.listar()

def buscar_por_id(prod_id: int) -> Optional[ProductoRow]:
    return productos_repo.obtener_por_id(prod_id)

def actualizar(prod_id: int, nombre: str, descripcion: str, cantidad: int, precio: float, categoria: str) -> int:
    _validar(nombre, cantidad, precio)
    return productos_repo.actualizar(prod_id, nombre.strip(), descripcion.strip(), cantidad, precio, categoria.strip())

def eliminar(prod_id: int) -> int:
    return productos_repo.eliminar(prod_id)

def buscar_por_texto(texto: str) -> List[ProductoRow]:
    if not texto.strip():
        return []
    return productos_repo.buscar_like(texto)

def reporte_stock_bajo(limite: int) -> List[ProductoRow]:
    if limite < 0:
        raise ValueError("El límite no puede ser negativo.")
    return productos_repo.stock_bajo(limite)
