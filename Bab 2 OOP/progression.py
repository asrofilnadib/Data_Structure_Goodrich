class Progression:
	def __init__(self, start=0):
		self._current = start
		
	def _advanced(self):
		"""update self._current to new value"""
		self._current += 1
	
	def __next__(self):
		if self._current is None:
			raise StopIteration()
		else:
			answer = self._current
			self._advanced()
			return answer
	
	def __iter__(self):
		return self
	
	def print_progress(self, n):
		"""print the value of progress"""
		print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProression(Progression):
	def __init__(self, increment=1, start=0):
		super().__init__(start)
		self._increment = increment
	
	def _advanced(self):
		self._current += self._increment


class GeometricProgression(Progression):
	def __init__(self, base=2, start=1):
		super().__init__(start)
		self._base = base
	
	def _advanced(self):
		self._current *= self._base


class FibonacciProgression(Progression):
	def __init__(self, first=0, second=1):
		super().__init__(first)
		self._prev = second - first
	
	def _advanced(self):
		self._prev, self._current = self._current, self._prev + self._current
		

if __name__ == '__main__':
	print("Progression Defult")
	Progression().print_progress(10)
	
	print("\nProgresi Aritmatik dengan increment 5")
	ArithmeticProression(5).print_progress(10)
	
	print("\nProgresi Aritmatik dengan increment 5 dimulai dari 2")
	ArithmeticProression(5, 2).print_progress(10)
	
	print("\nProgresi Geometri")
	GeometricProgression().print_progress(10)
	
	print("\nProgresi Geometri dengan pangkat 3")
	GeometricProgression(3).print_progress(10)
	
	print("\nProgresi Fibonacci")
	FibonacciProgression().print_progress(10)
	
	print("\nProgresi Fibonacci dengan nilai awal 4 dan 6")
	FibonacciProgression(4, 6).print_progress(10)
	
		