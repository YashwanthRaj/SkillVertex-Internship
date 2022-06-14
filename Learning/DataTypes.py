'''
Variables and Datatypes

1) None Types - None
2) Number Types - integer , float
3) Boolean Types - boolean (True/False)
4) Sequence Types - string , list , set , tuple
5) Mapping types

'''

# None type

my_variable = None
print(type(my_variable))

# Variables declaration

a = 'Yashwanth'
print(a)

b = 10
print(b)
c = 20
z=b+c
print(z)

# Concatenation

m = 'Hello'
n='World'
p=m+n
print(p)

# TypeCasting - Changing from one datatype to another

bo = 10
mo=str(bo)
xo = 20
xoo = str(xo)
print(type(bo))
print(type(mo))

print(type(xo))
print(type(xoo))

# Entering User Input (Default it will take it as string )

name = input('Enter your name: ')
classA = int(input("Enter your class: "))      # Specifying it as int

print("Name and class are: ",name,' , ',classA,'th ')