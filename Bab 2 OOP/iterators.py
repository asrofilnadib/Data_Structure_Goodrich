class Iterator:
	def __init__(self, sequence):
		"""buat iterator untuk memberi sequence/urutan"""
		self._seq = sequence
		self._k = 1
	
	def __next__(self):
		self._k += 1
		if self._k > len(self._seq):
			raise StopIteration
		else:
			return self._seq[self._k]
	def __iter__(self):
		return self
