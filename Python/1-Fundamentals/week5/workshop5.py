import random

def guess_random_number(tries, start, stop):
    rand_number = random.randint(start, stop)
    while tries != 0:
        print("remaining tries: " + str(tries))
        guess = int(input("guess the number: "))
        if guess < rand_number:
            print("number too low.")
            tries -= 1
        elif guess > rand_number:
            print("number too high")
            tries -= 1
        else:
            print("success!")
            break

    if tries == 0:
        print("sorry! You are out of tries.")


def guess_random_num_linear(tries, start, stop):
    rand_num = random.randint(start,stop)
    for x in range(tries):
        print("number of tries left: " + str(tries - x))
        print("guess: " + str(x))
        if x == rand_num:
            print("success!")
            return x
    print("failure")
    return -1

def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start,stop)
    for x in range(tries):
        pivot = int((start + stop)/2)
        if pivot == random_num:
            print("success!", pivot)
            return pivot
        elif pivot > random_num:
            stop = pivot -1
        else:
            start = pivot +1
        print("guess: ", pivot)
    print("failure")
    print(random_num)








''' Test task 1
guess_random_number(5,1,10)

    Test task 2


guess_random_num_linear(5,0,10)

    Test task 3
guess_random_num_binary(5,0,100)
'''
