
def show_balance(balance):
    print("Your balance is: " + str(balance))

def deposit(balance):
    amount = input("Enter the amount that you would like to deposit: ")
    return float(amount) + balance

def withdraw(balance):
    amount = input("Enter the amount that you would like to withdraw: ")
    if(float(amount) <= balance):
        return balance - float(amount)
    else:
        print("Denied. Widthdraw amount is larger than balance.")

def logout(name):
    print("Goodbye, " + name)