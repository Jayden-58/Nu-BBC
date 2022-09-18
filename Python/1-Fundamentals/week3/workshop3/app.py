from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database  = {"admin":"password123"}
donations = []
authorized_user = ""
while True:

    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print("you are logged in as: " + authorized_user)

    choice = input("choose an option: ")
    if choice == "1":
        login_username = input("enter username: ")
        login_password = input("enter password: ") 
        authorized_user = login(database, login_username, login_password)
       
    if choice == "2":
        register_username = input("enter a new username to register: ")
        register_password = input("enter a new password to register: ")
        if len(register_password) >= 5:
            authorized_user = register(database, register_username)
        else:
            print("password must be 5 or more characters")
        
        if authorized_user is not "":
            database[str(register_username)] =  str(register_password)
            print("success! username: " + authorized_user + " is now registered!")
    if choice == "3":
        if authorized_user == "":
            print("you are not logged in!")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    if choice == "4":
        show_donations(donations)
    if choice == "5":
        authorized_user = ""
        print("successfully logged out.")
    if choice == "6":
        print("Goodbye")
        exit()


