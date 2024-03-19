from typing import Generic, TypeVar, Optional
from copy import copy

T = TypeVar('T')

class Nodo(Generic[T]):
	def __init__(self, dato: T, sig: Optional["Lista"] = None):
		self.dato = dato
		if sig is None:
			self.sig= Lista()
		else:
			self.sig = sig

class Lista(Generic[T]):
	def __init__(self):
		self._head: Optional[Nodo] = None

	def es_vacia(self) -> bool:
		return self._head is None

	def head(self) -> T:
		if self.es_vacia():
			raise IndexError('lista vacia')
		else:
			return self._head.dato

	def tail(self) -> "Lista":
		if self.es_vacia():
			raise IndexError('lista vacia')
		else:
			return copy(self._head.sig)

	def insertar(self, dato: T):
		if self.es_vacia():
			self._head = Nodo(dato)
		else:
			actual = copy(self)
			self._head = Nodo(dato, actual)

	def eliminar(self, valor: T):
		if not self.es_vacia():
			if self.head() == valor:
				self._head = self._head.sig
			else:
				self._head.sig._eliminar_interna(self, valor)

	def _eliminar_interna(self, previo: "Lista", valor: T):
		if not self.es_vacia():
			if self.head() == valor:
				previo._head.sig = self._head.sig
			else:
				self._head.sig._eliminar_interna(self, valor)

	def ultimo(self) -> T:
		if self.es_vacia():
			raise IndexError('lista vacia')
		elif self.tail().es_vacia():
			return self.head()
		else:
			return self.tail().ultimo()

	def join(self, separador: str = '') -> str:
		if self.es_vacia():
			return ''
		elif self.tail().es_vacia():
			return str(self.head())
		else:
			return str(self.head()) + separador + self.tail().join(separador)

	def __repr__(self):
		return f'[{self.join(", ")}]'

	# Metodos para asemejarla a Sequence
	def __getitem__(self, indice):
		if indice >= len(self) or indice < 0: 
			raise IndexError("Indice fuera de rango")
		elif indice == 0:
			return self.head()
		else:
			return self.tail().__getitem__(indice - 1)

	def __len__(self):
		if self.es_vacia():
			return 0
		else:
			return 1 + self.tail().__len__()

xs: Lista[int] = Lista()

print(f'xs es vacia? {xs.es_vacia()}')	# True

# Operaciones basicas
xs.insertar(4)
xs.insertar(10)
xs.insertar(20)
xs.insertar(30)
xs.insertar(40)
ys = xs.tail()
ys.insertar(9)
ys.eliminar(10)
ys.insertar(8)

print(f'xs: {xs}')						# [40, 30, 20, 4]
print(f'ys: {ys}')						# [8, 9, 30, 20, 4]
print(f'xs es vacia? {xs.es_vacia()}')	# False
print(f'ultimo(xs): {xs.ultimo()}')		# 4
print(f'cabeza(xs): {xs.head()}')       # 40
print(f'cola(xs): {xs.tail()}')         # [30, 20, 4]
print(f'len(xs): {len(ys)}')			# 3
print(f'xs[0]: {xs[0]}')				# 40
print(f'xs[2]: {xs[2]}')                # 20
print(repr(xs))                         # [40, 30, 20, 4]

# Consumiendo como iterable
for x in xs:
  print(x)	# 40 -> 30 -> 20 -> 4
