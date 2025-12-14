from typing import Optional, List, Tuple
from backend.core.db import get_connection

ProductoRow = Tuple[int, str, str, int, float, str]

def crear(nombre: str, descripcion: str, cantidad: int, precio: float, categoria: str) -> int:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, cantidad, precio, categoria))
        conn.commit()
        return cur.lastrowid

def listar() -> List[ProductoRow]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos
            ORDER BY id ASC
        """)
        return cur.fetchall()

def obtener_por_id(prod_id: int) -> Optional[ProductoRow]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos WHERE id = ?
        """, (prod_id,))
        return cur.fetchone()

def actualizar(prod_id: int, nombre: str, descripcion: str, cantidad: int, precio: float, categoria: str) -> int:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, prod_id))
        conn.commit()
        return cur.rowcount

def eliminar(prod_id: int) -> int:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM productos WHERE id = ?", (prod_id,))
        conn.commit()
        return cur.rowcount

def buscar_like(texto: str) -> List[ProductoRow]:
    patron = f"%{texto.strip()}%"
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos
            WHERE nombre LIKE ? OR categoria LIKE ?
            ORDER BY id ASC
        """, (patron, patron))
        return cur.fetchall()

def stock_bajo(limite: int) -> List[ProductoRow]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT id, nombre, descripcion, cantidad, precio, categoria
            FROM productos
            WHERE cantidad <= ?
            ORDER BY cantidad ASC, id ASC
        """, (limite,))
        return cur.fetchall()
