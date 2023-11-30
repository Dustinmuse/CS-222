class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = float(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None # returning something that has no value

        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None

        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None  # returning something that has no value

        if amountToWithdraw < 0:
            print('You cannot deposit a negative amount')
            return None

        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None

        self.balance = self.balance - amountToWithdraw
        return self.balance

    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None  # returning something that has no value
        return self.balance

    def show(self):
        print('Name:', self.name)
        print('Balance:', self.balance)
        print('Password:', self.password)
        print()

def main():
    alice = Account("Alice Jones", 2000, "password")
    bob = Account("Bob Smith", 1000, "ballstate")
    customers = [alice, bob]
    customers[1].show()
    alice.show()
    alice.deposit(1000, "passwrd")
    alice.show()
    alice.deposit(1000, "password")
    alice.show()
    alice.withdraw(-1000, "password")
    alice.show()
    alice.withdraw(5000, "password")
    alice.show()
    alice.withdraw(500, "password")
    alice.show()

main()
