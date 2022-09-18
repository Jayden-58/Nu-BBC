import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    selection = input("input 'c' to pick a card, or 'q to quit: ")
    if selection == "c":
        card_draw = random.randint(0, (len(diamonds) - 1))
        hand.append(diamonds[card_draw])
        diamonds.pop(card_draw)
        print("your hand: ")
        print(hand)
        print("remaining cards")
        print(diamonds)
    elif selection == 'q':
        break
    else:
        print("INVALID INPUT.")

if not diamonds:
    print("no more cards")
