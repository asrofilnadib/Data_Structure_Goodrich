from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
	@abstractmethod
	def __len__(self):
		pass
	
	@abstractmethod
	def __getitem__(self, item):
		pass
	
	def __contains__(self, item):
		for j in range(len(self)):
			if self[j] == item:
				return True
		return False
	
	def index(self, value):
		for j in range(len(self)):
			if self[j] == value:
				return j
		raise ValueError("Nilai tidak sama")
	
	def count(self, val):
		k = 0
		for j in range(len(self)):
			if self[j] == val:
				k += 1
		return k