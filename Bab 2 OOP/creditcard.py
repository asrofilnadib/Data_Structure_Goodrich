class CreditCard:
    __slots__ = '_customer', '_bank', '_acnt', '_limit', '_balance'
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_acnt(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance = amount
      

if __name__ == '__main__':
    nasabah = []
    nasabah.append(CreditCard('Joni Sukmo',
                              'BCA', '0273 2849 7182 8201', 2500))
    nasabah.append(CreditCard('Windiarti',
                              'Bank Syariah', '0828 7839 7739 1728', 3500))
    nasabah.append(CreditCard('Suwarti Saman',
                              'BRI', '0784 7728 1116 8392', 4000))

    for val in range(1, 17):
        nasabah[0].charge(val)
        nasabah[1].charge(2*val)
        nasabah[2].charge(3*val)

    for c in range(3):
        print('Customer = ', nasabah[c].get_customer())
        print('Bank = ', nasabah[c].get_bank())
        print('Account = ', nasabah[c].get_acnt())
        print('Limit = ', nasabah[c].get_limit())
        print('Balance = ', nasabah[c].get_balance())
        while nasabah[c].get_balance() > 100:
            nasabah[c].make_payment(100)
            print('New Balance = ', nasabah[c].get_balance())
        print()
