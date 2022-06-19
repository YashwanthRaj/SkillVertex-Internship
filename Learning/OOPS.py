'''

Object Oriented Programming

Contains Class and Objects
Objects are the real world entity
Class are the blueprint of the class

Constructor is used to initialize variables

We create Class with parameters , then we create default constructor to initialize all the variables , then function to act
then we create object with given parameters to call and use the class

'''

# Student details example

class student:          # Creation of Class

    def __init__(self,f_name,l_name,dob,Degree):     # Creation of Default Constructor
        self.f_name = f_name
        self.l_name = l_name
        self.dob = dob
        self.Degree = Degree

    def FullName(self):                 # Creation of Function inside Classs
        print(f"Your Funn Name is {self.f_name} {self.l_name} \n")

    def Details(self):
        print(f'The details of student {self.f_name} are:-')
        print(f'Degree: {self.dob} ')
        print(f'Programme: {self.Degree}')

obj1 = student('Yashwanth','Raj','25/05/2002','B Tech')      # Creating Object to access the Class
obj2 = student('Sai Nikhil','Varadha','04/10/1990','B Tech')
obj1.FullName()  # operating the function inside the class
obj2.Details()
print('\n')

# Calculator Example

class calculator:
    def __init__(self,int1,int2,funct):
        self.int1 = int1
        self.int2  = int2
        self.funct = funct

    def Addition(self):
        return (self.int1 + self.int2)

    def Subtraction(self):
        return(self.int1 - self.int2)

    def Mult(self):
        return(self.int1 * self.int2)

    def Div(self):
        return(self.int1 / self.int2)

a = int(input("Enter first number: "))
b = int(input("Enter the second number: "))
c = input("Enter the operation: ")

obj1 = calculator(a,b,c)
if c == 'add':
    print(obj1.Addition())
elif c == 'Subtract':
    print(obj1.Subtraction())
elif c == 'Multiply':
    print(obj1.Mult())
elif c == 'Divide':
    print(obj1.Div())
else:
    print("Operation Not Verified!! ")

# Car Example

class car:
    def __init__(self,name,fuel,milage,range):
        self.name = name
        self.fuel = fuel
        self.milage = milage
        self.range = range

    def fuelsta(self):
        if self.range <= (self.milage * self.fuel):
            print(f"Enough Fuel present in your car {self.name}!!")
        else :
            print(f'You need to fuel your {self.name}!!')

car1 = car('Honda City',20,20,500)
car1.fuelsta()
print('\n')

car2 = car('Skoda Rapid',30,15,60)
car2.fuelsta()




