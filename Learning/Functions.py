'''

Functions
Functions are user defined blocks of Statements that are used whenever the function is called

syntax:
def fun_name(condition , parameter):
    body

function call
fun_name()

Recursion is function calling itself

'''
# Call withouut return value
def functiona():
    a=12
    b=13
    print(a+b)

functiona()  # Calling Function


# call with return value
def funct():
    a=int(input("enter the number1 : "))
    b=int(input("enter the number2 : "))
    return a+b

c=funct()
print(c)


# Call Function with parameter
def Additiona(m,n):
    d = m+n
    return d

sum1 = Additiona(4,8)
print(sum1)

# Default parameter
def deffun(a=12,b=34):
    print(a+b)

deffun(45)
deffun(34,78)

# Arbitrary arguements
def funab(*args):
    return(args)

print(funab(10,11,12,1,41,51,46,456,46,46))
print(funab(45,45,45,78,78,78,78))

# Recursion
def recfun():
    k = 10
    l = 20
    recfun()
    print(k+l)

# Recursion Example like factorial

def factfun(n):
    if n==1 or n == 0:
        return 1
    else:
        return n*factfun(n-1)

print(factfun(5))