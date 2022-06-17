'''

Sequence Datatypes are the Datatypes that can store multiple values or sequence of values under single variable name
Some of Widely used Sequence Datatypes in Python are List , Tuple , set , String etc
We are including String here because it has very similar characteristics

Indexing in Python starts from 0
'''

# STRING and its operations

name = 'Yashwanth'
print(name[5])
print(name[-1]) # Will return the last number/char
print(name[:4]) # Slicing , here last number is not considered

nameHalf = name[4:]
print(nameHalf)

print(name[1:-2:3]) # [start: stop: step value] actual jump size = entered value -1

# LIST

L1 = [1 , 'Vikram' , 10.32 , True]

print(type(L1))
print('The first element is:',L1[0])
print('The last  element is:',L1[-1])

L1.insert(3,'Beast') # Insert needs position also , as list is ordered
print(L1)

L1.append("vainko")  # Inserts the element at the last
print(L1)

L2 = ['Jaidev' , False]
L1.extend(L2)  # Adds another list
print(L1)

L2[0] = True  # Updating the values in a string
print(L2)

print(L1)
L1.remove('Vikram')
print(L1)

L1.pop(0)  # Removing by Index Position
print(L1)

print(L2)
L2.clear()
print(L2)  # We will get an empty list

del L1[2]
print(L1)
del L1
print(L1)  # Will throw error or print nothing because now Entire list with its Variable is deleted
