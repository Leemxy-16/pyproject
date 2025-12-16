#a program that collect expense amd also check budget
budget = int(input("Enter your total budget: "))
expense = {}
total = 0
answer = ' new'

while answer != 'stop':
    item = input("Enter the expense item: ")
    cost = float(input(f"Enter the cost for {item}: "))
    expense[item] = cost
    total += cost
    answer = input(
        "Type 'stop' to finish or press Enter to add another expense: ").lower()

for i in expense.items():
    print(f"The cost of {i[0]} is {i[1]}")
print(f"Your total expenses amount to: {total}")

if (budget < total):
    print(
        f"You have exceeded your ${budget}. Your total expenses are ${total}.")
elif (budget > total):
    print(
        f"You are within your budget of ${budget}. Your total expenses are ${total}.")
else:
    print(
        f"You have exactly met your budget of ${budget}. Your total expenses are ${total}.")
>>>>>>> d03e48048e32dc0bb94f4961294f44f6395fee83
