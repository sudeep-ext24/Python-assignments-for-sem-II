#BankAccHandling.prg

class BankAccount:

    def __init__(self, acc_no , balance =0):
        self.acc_no = acc_no
        self.balance = balance


    def deposit(self):
        amnt= float(input("Enter an amount:"))

        if amnt>0:
            self.balance += amnt
            print(f"{amnt} deposited successfully.")
            print(f"{self.balance} is your current balance.")
        else:
            print("wrong amount is entered.")

    def withdraw(self):
        amnt= float(input("Enter an amount:"))

        if amnt>0:
            if amnt <= self.balance:
                self.balance -= amnt
                print(f"{amnt} is debitted from your account.")
                print(f"{self.balance} is your current balance.")
            else:
                print("insufficient balance.")
        else:
            print("wrong amount is entered.")

    def check_balance(self):
        print(f"{self.balance} is your current balance.")

acc_no = int(input("enter acc number:"))
balance= float(input("enter initial balance:"))
obj= BankAccount(acc_no, balance)

print("1. Deposit")
print("2. Withraw")
print("3. Check Balance")
print("4. Exit")

while True:
    choice= int(input("enter a choice:"))

    if choice == 1:
        obj.deposit()
    elif choice == 2:
        obj.withdraw()
    elif choice == 3:
        obj.check_balance()
    elif choice == 4:
        print("thank you.")
    else:
        print("error.")
    
    break

print("end.")