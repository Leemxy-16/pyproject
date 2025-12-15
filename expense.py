#a program that collect expense amd also check budget
budget = int(input('enter your budget make it a number'))
expenses = {}
total = 0
answer = 'new'

while answer != 'stop':
    name = input('enter your expense name')
    amount = int(input('enter the amount of your expenses'))
    total += amount
    expenses[name]= amount
    answer= input('enter stop to exist and new to continue')

for x in expenses:
    print(f'{x} amount : {expenses[x]}')

print(f' your total expenses is ${total}')

if (budget < total):
    print(f'you are above your ${budget} bugdet, \n you are too broke to be spending those money')
else:
    print(f'you are within your ${budget}')