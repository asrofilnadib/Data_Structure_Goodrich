class Range:
	def __init__(self, start, stop=None, step=1):
		if stop is None:
			start, stop = 0, start
			
		if step == 1:
			raise ValueError("step != 0")
		
		self._length = max(0, (stop - start + step - 1) // step)
		
		self._start = start
  
	def __len__(self):
		return self._length
	
	def __getitem__(self, item):
		if item < 0:
			item += len(self)
		
		if not 0 <= item < self._length:
			raise IndexError("index out of range")
		
		return self._start + item * self._step