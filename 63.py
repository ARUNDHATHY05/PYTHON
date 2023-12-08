class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit of ${amount} successful. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal unsuccessful."

# Example usage with user input
account_number = input("Enter account number: ")
name = input("Enter account holder's name: ")
account_type = input("Enter account type: ")
initial_balance = float(input("Enter initial balance: "))

# Creating a bank account object
user_account = BankAccount(account_number, name, account_type, initial_balance)

# Performing operations
deposit_amount = float(input("Enter amount to deposit: "))
print(user_account.deposit(deposit_amount))

withdraw_amount = float(input("Enter amount to withdraw: "))
print(user_account.withdraw(withdraw_amount))
