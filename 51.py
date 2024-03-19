from typing import List, TypeAlias

__all__ = ['Nat', 'cero', 'suc', 'suma', 'producto']

Nat: TypeAlias = List[int]

def cero() -> Nat:
    return []

def suc(n: Nat) -> Nat:
    return [0] + n

def nat_to_int(n: Nat) -> int:
    return len(n)

def suma(x: Nat, y: Nat) -> Nat:
    if not x:
        return y
    else:
        return [0] + suma(x[1:], y)
    
def producto(x: Nat, y: Nat) -> Nat:
    if not y:
        return []
    else:
        print(f'x={x},y={y}') 
        return suma(x, producto(x, y[:-1]))

if __name__ == '__main__':
    n1: Nat = cero()                # n1 = 0
    n2: Nat = suc(suc(suc(n1)))     # n2 = 3
    n3: Nat = suc(suc(n2))          # n3 = 5
    print(n1)                       # []
    print(n2)                       # [0, 0, 0]
    print(n3)                       # [0, 0, 0, 0, 0]
    n4: Nat = suma(n2, n3)          # n4 = 8
    print(n4)                       # [0, 0, 0, 0, 0, 0, 0, 0]
    print(producto(n2, n3))         # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]