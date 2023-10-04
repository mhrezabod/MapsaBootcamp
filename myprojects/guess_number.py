import random

x = int(input("pls get us a number: "))
random_number = random.randint(1, x)

def guess():

    myguess = 0
    while random_number != myguess:

        myguess = int(input("what do you guess? "))

        if myguess > random_number:
            print("not a percies guess! try lower one")
        elif myguess < random_number:
            print("try a higher one")

        else:
            print(f"yay! the {myguess} number is the correct")

guess()