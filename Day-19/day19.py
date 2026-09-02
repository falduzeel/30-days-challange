class BankAccount:
    """Class representing a simple bank account."""

    bank_name = "Python National Bank"

    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.transaction_history = []
        self._add_to_history(f"Account opened with initial balance: ${initial_balance:.2f}")

    def _add_to_history(self, record: str):
        """Helper method to record account transactions."""
        self.transaction_history.append(record)

    def deposit(self, amount: float) -> float:
        """Deposits a positive amount into the account."""
        if amount <= 0:
            print("❌ Deposit amount must be greater than zero.")
            return self.balance

        self.balance += amount
        self._add_to_history(f"Deposited: ${amount:.2f}")
        print(f"✅ Successfully deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        return self.balance

    def withdraw(self, amount: float) -> float:
        """Withdraws an amount if sufficient funds exist."""
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
            return self.balance
        
        if amount > self.balance:
            print(f"❌ Insufficient funds! Current balance is ${self.balance:.2f}")
            return self.balance

        self.balance -= amount
        self._add_to_history(f"Withdrew: ${amount:.2f}")
        print(f"✅ Successfully withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")
        return self.balance

    def display_statement(self):
        """Prints a detailed transaction log for the account."""
        print(f"\n--- Account Statement for {self.owner} ({self.bank_name}) ---")
        for idx, entry in enumerate(self.transaction_history, start=1):
            print(f"{idx}. {entry}")
        print(f"Current Balance: ${self.balance:.2f}\n" + "-" * 45)


if __name__ == "__main__":
    alice_acc = BankAccount("Alice", 500.0)
    bob_acc = BankAccount("Bob", 150.0)

    alice_acc.deposit(250.0)
    alice_acc.withdraw(100.0)
    alice_acc.withdraw(1000.0)

    bob_acc.withdraw(50.0)

    alice_acc.display_statement()
    bob_acc.display_statement()