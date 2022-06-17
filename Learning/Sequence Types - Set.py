'''

A set Sequence Datatype may contain multiple different datatypes and it does not Allow Duplicate ,
Unindexed or Unordered , Unchangable .

'''

m1 = {1 , 23, 'HelloWorld'} # Creation of Set
print(type(m1))
m2=set() # Creation of Empty set
print(type(m2))

am1 = {} # As Dictionary also has {} , empty set cannot be declared ans {} alone
print(type(am1))

# Adding Values in a list
m1.add("GitHub")
print(m1)

# Update method used to add sequence Datatype (List , tuple , etc)
m3={12,"manya",54}
m1.update(m3)
print(m1)

# Methods available to remove , delete values are - remove , discard , pop

m1.remove('HelloWorld')  # Remove takes value that needs to be removed
print(m1)

m1.discard('HelloWorld')
print(m1)

'''
The difference between discard and remove is that if the given element is not present in the set 
> DISCARD will not throw an error  
> remove will throw an error
'''

m1.pop() # As no indexing , it will remove the last element that was added
print(m1)