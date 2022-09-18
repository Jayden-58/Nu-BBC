# traits
name = "name"
hunger = 0
thirst = 0



def check_alive():

    dead = False
    if(hunger > 100):
        dead = True
    elif(thirst > 100):
        dead = True
    else:
        dead = False
    
    if(dead == True):
        print("player has died")
    return dead
def eat(hunger):
    hunger = hunger - 15
    return hunger

def drink(thirst):
    thirst = thirst - 15
    return thirst

def consume_energy(hunger, thirst):
    hunger = hunger + 10
    thirst = thirst + 17
    return hunger, thirst

while(check_alive() == True):
    consume_energy(hunger, thirst)