from operator import truediv
from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# register
print("          === Automated Teller Machine ===          ")
while (True):
    reg_name = input("enter name to register: ")
    if(len(reg_name) < 1 or len(reg_name) > 10):
        print("invalid name, Name must be more than 1 character and less than 10 characters")
    else:
        user = reg_name
        break

while(True):
    reg_pin = input("Enter PIN: ")
    if(len(reg_pin) == 4):
        pin = reg_pin
        break
    else:
        print("Invalid PIN. PIN must be four characters")

balance = 0.0
print(user + " has been registered to with a starting balance of: $" + str(balance))
# login
print("          === Automated Teller Machine ===          ")
login_success = False
while login_success == False:
    name_to_validate = input("Enter Name: ")
    pin_to_validate = input("Enter PIN: ")
    if(name_to_validate.lower() == user.lower() and str(pin_to_validate) == str(pin)):
        login_success = True
    else:
        print("Invalid Login Details. Please try again")
        login_success = False

# ATM Menu

while(True):
    atm_menu(user)
    option = input("Choose an option: ")
    if(int(option) == 1):
        account.show_balance(balance)
    elif(int(option) == 2):
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif(int(option) == 3):
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif(int(option) == 4):
        account.logout(user)
        break
    else:
        print("Invalid Option")
