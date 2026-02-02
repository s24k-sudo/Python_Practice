class Bank:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount

    def withdrawal(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount


account = Bank()
print(account.balance)  
account.deposit(200.00)
print(account.balance)
account.withdrawal(200.00)
print(account.balance)
account.deposit(400)
print(account.balance)

