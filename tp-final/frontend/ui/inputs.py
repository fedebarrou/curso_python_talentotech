from typing import Optional

def input_no_vacio(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("El valor no puede estar vacío.")

def input_int(prompt: str, min_val: Optional[int] = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            n = int(raw)
            if min_val is not None and n < min_val:
                print(f"Debe ser un entero >= {min_val}.")
                continue
            return n
        except ValueError:
            print("Ingrese un número entero válido.")

def input_float(prompt: str, min_val: Optional[float] = None) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            n = float(raw)
            if min_val is not None and n < min_val:
                print(f"Debe ser un número >= {min_val}.")
                continue
            return n
        except ValueError:
            print("Ingrese un número válido.")

def pausar() -> None:
    input("\nPresione Enter para continuar...")
