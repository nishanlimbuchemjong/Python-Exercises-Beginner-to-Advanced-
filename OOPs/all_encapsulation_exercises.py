# Q.1: Create a class BankAccount with private attributes _balance and _account_number
"""
Input:
Deposit: $1000, Withdraw: $500

Output:
Balance after deposit: $1000
Balance after withdrawal: $500

"""
print("Question-1:\n")

class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number
    
    # method for showing the current balance on bank account
    def show_balance(self):
        return self.__balance

    # method to depost/account amount into bank account
    def deposit(self, amount):
        return self.__balance + amount

    # method for withdrawal amount from bank account
    def withdrawal(self, amount):
        return self.__balance - amount

# creating an instance of class 'BankAccount'
detail =  BankAccount(50000, 1)

# calling show_balance() method for showing the balance
print(f"Your balance : {detail.show_balance()}")

# calling depost() method for depositing the balance
print(f"After depositing an amount = 10000")
print(f"\n\tYour balance : {detail.deposit(10000)}")


# calling withdrawal() method for withdrawalling the balance from the bank account
print(f"After withdrawalling an amount = 500:")
print(f"\n\tYour balance : {detail.withdrawal(500)}")

print("..................................................................................\n")
