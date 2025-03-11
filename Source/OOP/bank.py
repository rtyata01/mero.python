class Account:
    """Represents a simple bank account with deposit and withdrawal functionality."""

    def __init__(self):
        self._balance = 0

    @property
    def balance(self) -> float:
        """Returns the current account balance."""
        return self._balance

    def withdraw(self, amount: float):
        """Withdraws money from the account if sufficient balance is available."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        
        if amount > self._balance:
            print("Insufficient funds! Withdrawal denied.")
        else:
            self._balance -= amount
            print(f"Successfully withdrew {amount}. New balance: {self._balance}")

    def deposit(self, amount: float):
        """Deposits money into the account if the amount is positive."""
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        
        self._balance += amount
        print(f"Successfully deposited {amount}. New balance: {self._balance}")

# Test Cases
account = Account()
print(f"Initial Balance: {account.balance}")  # Uses the @property

account.deposit(10000)
print(f"Balance after deposit: {account.balance}")

account.withdraw(-50000)  # Invalid withdrawal
account.withdraw(10000)  # Valid withdrawal
print(f"Balance after withdrawal: {account.balance}")

account.deposit(5000)
account.withdraw(5000)
print(f"Final Balance: {account.balance}")
