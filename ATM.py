'''
Task 3 : ATM simulator
Create a program that simulates the all atm
functionalities and operations (Check balance,
Deposit, Withdraw)

'''
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount} successfully. New balance: {self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount} successfully. New balance: {self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            return "Insufficient balance."

def main():
    atm = ATM()

    while True:
        print("ATM Simulator")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Quit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            print("Current balance:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM simulator!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
