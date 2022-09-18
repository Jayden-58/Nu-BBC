import random
high_score  = 0


def dicegame():
    global high_score
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print("you rolled a... " + str(dice1))
    print("you rolled a... " + str(dice2))
    print("you have rolled a total of: "  + str(total))
    if(total > high_score):
        print("New high score!")
        
        high_score = total
    print("your high score is: " + str(high_score))
    

while(True):
    print("1) Roll Dice")
    print("2) Leave game")
    choice =  input("Enter your choice: ")
    if(int(choice) == 1):
        dicegame()
    elif(choice == 2):
        break