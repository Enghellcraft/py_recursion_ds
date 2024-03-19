from typing import TypeAlias, Union

Nat: TypeAlias = Union["Cero", "Suc"]

# Clases constructoras de estructura
class Cero:
  def __repr__(self):
    return 'Cero'

  def __str__(self):
    return '0'

class Suc:
  def __init__(self, pred: Nat):
    self.pred = pred

  def __repr__(self):
    if isinstance(self.pred, Cero):
      return 'Suc(Cero)'
    else:
      return f'Suc({self.pred.__repr__()})'

  def __str__(self):
    return str(nat_to_int(self))

# Operaciones
def cero() -> Nat:
  return Cero()

def es_cero(n: Nat) -> bool:
  return isinstance(n, Cero)

def suc(n: Nat) -> Nat:
  return Suc(n)

def pred(n: Nat) -> Nat:
  if es_cero(n):
    raise ValueError('cero no tiene predecesor')
  else:
    return n.pred

def nat_to_int(n: Nat) -> int:
  if es_cero(n):
    return 0
  else:
    return 1 + nat_to_int(pred(n))

def suma(x: Nat, y: Nat) -> Nat:
  if es_cero(x):
    return y
  else:
    return suma(pred(x), suc(y))

def producto(x: Nat, y: Nat) -> Nat:    
    if isinstance(y, Cero):        
        return cero()    
    else:  
        print(f'x={x},y={y}')      
        return suma(x, producto(x, y.pred))

if __name__ == '__main__':   

    n1: Nat = cero()                                  # n1 = 0    
    n2: Nat = suc(suc(suc(n1)))            # n2 = 3    
    n3: Nat = suc(suc(n2))                     # n3 = 5    
    print(n1)                                               # 0    
    print(n2)                                              # 3    
    print(n3)                                              # 5   
    n4: Nat = suma(n2, n3)                   # n4 = 8    
    print(n4)                                              # 8   
    print(producto(n2, n3))                  # 15
    print(repr(n4))                                    #?????