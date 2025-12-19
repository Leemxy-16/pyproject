from random import random

player = input('do you want to play y/n')
dice = 6
dice  = random(0,6)
if player == 'y':
    print (dice)
else:
    print('thank you for your intrest')