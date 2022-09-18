class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
    def change_name(self, new_name):
        self.name = new_name
    def change_pin(self, new_pin):
        self.pin = new_pin
    def change_password(self, new_password):
        self.password = new_password
    
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    def show_balance(self):
        print(self.name + " has: " + str(self.balance))
    def withdrawl(self, amount_to_widthdrawl):
        self.balance = self.balance - amount_to_widthdrawl
    def deposit(self, amont_to_deposit):
        self.balance = self.balance + amont_to_deposit
    def transfer_money(self, user):
        pin = int(input("enter your pin: "))
        if self.pin == pin:
            amount = int(input("enter the amount you'd like to give: "))
            self.balance -= amount
            user.balance += amount
            return True
        else:
            print("invalid PIN. Transaction cancelled.")
            return False
    def request_money(self, user):
        amount_requested = int(input("Enter the amount of money you need from: " + user.name + "."))
        other_pin = int(input("Enter the user's pin to authorize this transaction: "))
        if user.pin == other_pin:
            other_password = input("Enter the user's password: ")
            if user.password == other_password:
                print("authenticated.")
                user.balance -= amount_requested
                self.balance += amount_requested
                return True
            else: 
                return False
        else:
            return False

            








"""Driver Code for Task 1 
test_person = User("bob", 1234, "password")
print(test_person.name + " " + str(test_person.pin) + " " + test_person.password) 
"""
""" Driver Code for Task 2 
test_person = User("bob", 1234, "password")
print(test_person.name + " " + str(test_person.pin) + " " + test_person.password)
test_person.change_name("jerry")
test_person.change_password("bruh")
test_person.change_pin(4567)
print(test_person.name + " " + str(test_person.pin) + " " + test_person.password)
"""
""" Driver Code for Task 3
test_bank_user = BankUser("bob", 1234, "password")
print(test_bank_user.name + " " + str(test_bank_user.pin) + " " + test_bank_user.password)
print(test_bank_user.balance)
"""
""" Driver Code for Task 4
test_bank_user = BankUser("bob", 1234, "password")
print(test_bank_user.name + " " + str(test_bank_user.pin) + " " + test_bank_user.password)
print(test_bank_user.balance)
test_bank_user.deposit(1000)
test_bank_user.withdrawl(250)
test_bank_user.show_balance()
"""
""" Driver Code for Task 5
test_bank_user = BankUser("bob", 1234, "password")
test_bank_user_2 = BankUser("amy", 1111, "password1")
print(test_bank_user.name + " " + str(test_bank_user.pin) + " " + test_bank_user.password)
print(test_bank_user_2.name + " " + str(test_bank_user_2.pin) + " " + test_bank_user_2.password)
test_bank_user.deposit(1000)
test_bank_user_2.deposit(500)
test_bank_user.show_balance()
test_bank_user_2.show_balance()
test_bank_user.transfer_money(test_bank_user_2)
test_bank_user.show_balance()
test_bank_user_2.show_balance()
test_bank_user.request_money(test_bank_user_2)
test_bank_user.show_balance()
test_bank_user_2.show_balance()
"""