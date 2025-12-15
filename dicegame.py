import random

while True :

    user_guess = input("play game? (y/n): ").lower()

    if user_guess == 'y':

        #print(f"({dic},{dic1})")

        dic2 = random.randint(1,6)
        dic1 = random.randint(1,6)
        print(f"({dic2},{dic1})")
    elif user_guess == 'n':
        print("thank you for playing")
        break


    else:
        print("invalid choice")
    




