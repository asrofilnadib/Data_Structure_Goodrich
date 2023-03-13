from creditcard import CreditCard

class PredatoryCreditCard(CreditCard):
	__slots__ = '_apr'
	OVERLIMITEDFEE = 5
	def __init__(self, customer, bank, acnt, limit, apr):
		"""Buat new predatory credit card
		
		The initial balance is zero
		
		customer = nama customer
		bank, nama bank
		acnt = no rekening
		limit = credit limit
		
		"""
		
		super().__init__(customer, bank, acnt, limit)
		sel._apr = apr
	
	def charge(self, price):
		"""Charge dari setiap transaksi, asumsikan bahwa
		credit limiit memadai
		
		return True jika di proses
		return False dan berikan sanksi $5 fee jika transaksi
		dibatalokan"""
		success = super().charge(price)
		if not success:
			self._balance += PredatoryCreditCard.OVERLIMITEDFEE
		return success
	
	def process_month(self):
		if self._balance > 0:
			monthly_factor = pow(11 + self._apr, 1/12)
			self._balance *= monthly_factor
		