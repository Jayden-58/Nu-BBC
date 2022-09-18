
def show_homepage():
    print('''
    
=== DonateMe Homepage ===
1. login    2. register
3. donate   4.show donations
5. logout   6.exit
=========================''')

def donate(username):
    donation_amount = input("input amount to donate, or '-1' to go back: ")
    if float(donation_amount) > 0:
        donation_string = (username + " donated " + str(float(donation_amount)))
        print("thank you for the donation!")
        return donation_string
    elif donation_amount == "-1":
        return None
    else:
        print("donation amount must be above 0")
        donate(username)

def show_donations(donations):
    print("\n--- All Donations ---")
    index = 0
    if donations:
        for x in donations:
            print(donations[index])
            index += 1
    else:
        print("currently there are no donations....")
        

