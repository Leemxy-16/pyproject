guest_list = ['zainab','maimuna','khadija']
for guest in guest_list:
    print(f"\thello {guest.title()}, you are invited to my dinner party")
    
guest_list[1]= "aisha"

for i in guest_list:
    print(f"\n hello {i.title()},you are invited to my dinner pary")

print("got a bigger table now need to add people")

guest_list.insert(0,"kaseem")
guest_list.insert(3,'farida')
guest_list.insert(5,'yusra')

for guests in guest_list:
    print(f"\thello {guests.title()},you are invited to a dinner")

#change of plan new table wont arrive on time
print('new table wont arrive on time')

print(len(guest_list))

poped_guest1 = guest_list.pop(3)
print(f'{poped_guest1.title()},sorry the table not enough')
poped_guest2 = guest_list.pop(4)
print(f'{poped_guest2.title()},sorry the table not enough')
poped_guest3 = guest_list.pop(3)
print(f'{poped_guest3.title()},sorry the table not enough')
poped_guest4 = guest_list.pop(0)
print(f'{poped_guest4.title()},sorry the table not enough')

print(len(guest_list))

for i in guest_list:
    print(f'\nhello {i.title()},you are invited to dinner')

del guest_list[1]
del guest_list[0]

print(guest_list)

