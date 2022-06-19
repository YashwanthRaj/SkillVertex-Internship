'''

For Loops
These Loops run until the given condition turns false

There are entry and exit controlled

Entry controlled are the one that are controlled by the entry given condition
>Check the condition :
    then body executed

Exit controlled are the one that are controlled by exit statements like break
>body executed , then condition checked


1) Entry based - (for,while)
2) Exit based - (do,while)


Control Statements:
1) pass
2) break - come out of the loop
3) continue  - Skipping over loop


syntax :
for i in range(a,b,c):  a is starting value included , b is ending value excluded , i.e we will consider b-1 be last c - step size
    body
'''

# Printing a table of 2
a=int(input("Enter the table that you want to have: "))

for i in range(1,11):
    print(f'{a} * {i} = {a*i} ')

# Weekday example

weekday=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

weekend=[]

for i in range(0,len(weekday)):
    print(weekday[i])
    if weekday[i]=='Saturday':
        weekend.append(weekday[i])
    elif weekday[i] == 'Sunday':
        weekend.append(weekday[i])

print("The weekends are: ",weekend)

# Names example
names=['Yashwanth','Sai Nikhil','Shrinivas','Sriram']
for i in names:
    print(i)
    if i == ' Yashwanth':
        print('Good Boy !!')

print('\n')
# Control statements
for i in range(0,5):
    if i==2:
        break
    print(i)

print('\n')

for j in range(0,5):
    if j == 3:
        continue
    print(j)



'''

While Loops
These Loops run until the given condition turns false

'''
i=0
while i < 10:
    print(i)
    i=i+1  # if this step not given , loop will run infinitely