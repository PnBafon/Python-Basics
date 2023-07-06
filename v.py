import math

persons = ['Shalom', 'Diana', ]
persons.insert(0,'Bafon')

# getting middle index of the list
length = len(persons)
if length % 2 == 0:
    middle = math.floor( ((length / 2) + (length /2 + 1)) / 2)
    print(middle)
else:
    middle = math.ceil(len(persons) / 2)

persons.insert(middle, 'Precious')
persons.append('Louis')

print('Hi everyone I just found a bigger dinner table! \n')

# invitint the persons now
for person in persons:
    print(f"Hello {person}, you are invited for the dinner party")


