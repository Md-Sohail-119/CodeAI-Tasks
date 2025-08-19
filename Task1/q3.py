class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Enter a valid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def transfer(self, amount, other):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other.balance += amount
            print(f"{amount} transferred from {self.name} to {other.name}. New balance: {self.balance}")
        else:
            print("Transfer failed: insufficient balance.")

    def check_balance(self):
        print(f"Account {self.acc_no} ({self.name}) has balance: {self.balance}")

    def __str__(self):
        return f"Account[{self.acc_no}] - Owner: {self.name}, Balance: {self.balance}"

account_a = BankAccount("A123", "Alice", 1000)
account_b = BankAccount("B456", "Bob", 500)

account_a.deposit(200)
account_a.withdraw(100)
account_a.transfer(300, account_b)
account_a.check_balance()

account_b.deposit(500)
account_b.withdraw(600)
account_b.transfer(1000, account_a)
account_b.check_balance()

print(account_a)
print(account_b)
