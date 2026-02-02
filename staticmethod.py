class Bank_Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s current balance is: {self._balance}")
        else:
            print("The amount must be positive")
    def withdrawal(self, ammount):
             self._balance -=ammount
             print(f"The new balence is {self._balance} ")

    @staticmethod
    def is_vaild_intrestrate(rate):
        return 0 <= rate < 5
    
account=Bank_Account("Soham", 0)
account.deposit(200000)


