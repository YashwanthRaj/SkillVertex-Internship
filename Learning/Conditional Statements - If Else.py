'''

If Else Conditional Statement
If condition in If block of code is correct then content inside If will work , or else Else block of code will work

Syntax :
if (condition):
    body
else:
    body

nested
if ():
elif():
elif():
elif():
else:

'''

# Example of simple if and else
num=int(input("Enter the number : "))

if num%2 == 0:   # % will return remainder
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd ")


# Example of two condition satisfying
anothernum = int(input("Enter another number: "))
if anothernum > 100 and anothernum < 200:
    print("The number is in between 100 and 200")
else:
    print("The number is not in range of 100 and 200")


# Example of nested if
anothernum2 = int(input("Enter another number: "))
if anothernum2 > 100 and anothernum2 < 200:
    print("The number is in between 100 and 200")
    if anothernum2 % 2 == 0:  # % will return remainder
        print(f"The number {anothernum2} is even")
    else:
        print(f"The number {anothernum2} is odd ")
else:
    print("The number is not in range of 100 and 200")


# Geading System Example for repeated if else
grade = int(input("Enter your percentage: "))

if grade>90:
    print("A")
elif grade>80:
    print("B")
elif grade>70:
    print("C")
elif grade>60:
    print("D")
elif grade>50:
    print("E")
else:
    print("Fail :(")

# Price Range using Dictionary
items = {200:['Mouse','Keyboard','mousepad'],500:['Earphones','Airpods','Lighter'],1000:['SSD','HDD','Caddy']}

pricerange = int(input('Enter your budget: '))

if pricerange >=1000:    # Without elif , it will print till all if condition satisfies
    print("The products are: ",items[1000])
if pricerange >=500:
    print("The products are: ",items[500])
if pricerange >=200:
    print("The products are: ",items[200])
else:
    print("Sorry but you are broke :(")


# Same example but we are printing in a same line
items1 = {200:['Mouse','Keyboard','mousepad'],500:['Earphones','Airpods','Lighter'],1000:['SSD','HDD','Caddy']}
itemsava=[]
pricerange1 = int(input('Enter your budget: '))

if pricerange1 >=1000:    # Without elif , it will print till all if condition satisfies
    itemsava.extend(items[1000])
if pricerange1 >=500:
    itemsava.extend(items[500])
if pricerange1 >=200:
    itemsava.extend(items[200])
else:
    print("Sorry but you are broke :(")

print(itemsava)