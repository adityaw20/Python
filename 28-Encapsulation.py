# Encapsulation  = Wrapping variables and methods together.
# We can hide data by using "_" or "__" for private members.

class bankaccount:
    def __init__(self,balance):
        self.__balance = balance # private variable
    
    def deposite(self,amount):
        self.__balance +=amount
        print(f"Deposited : {amount}")

    def withdraw(self , amount ):
        if amount <= self.__balance:
            print(f"Withdraw : {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# Usage #objects
acc = bankaccount(1000)
acc.deposite(500)
acc.withdraw(200)

print("Current Balance :",acc.get_balance())
# print(acc.__balance) # Error (cannot access directly)