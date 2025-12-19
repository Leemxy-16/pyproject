age = int(input('enter a age'))

if age < 2:
    print('baby')
elif age == 2 and age < 4:
    print('toddler')
elif age < 13:
    print('kid')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('elder')
