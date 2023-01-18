class Vector:
	def __init__(self, d):
		"""buat d-dimensional vektor dari 0"""
		self._cord = [0] * d
	
	def __len__(self):
		"""mengembalikan dimensi dari vektor"""
		return len(self._cord)
	
	def __getitem__(self, j):
		return self._cord[j]
	
	def __setitem__(self, key, value):
		"""mengembalikan koordinat dari vektor"""
		self._cord[key] = value
	
	def __add__(self, other):
		if len(self) != len(other):
			raise ValueError("dimension must agree")
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = other[j] + self[j]
		return result
	
	def __ne__(self, other):
		return not self == other
	
	def __str__(self):
		return '<' + str(self._cord)[1:-1] + '>'
		