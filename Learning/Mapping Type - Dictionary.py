'''

Dictionary{} - {Key1:value1 , Key2:Value2}
Dictionary is a Key Value pair
A key should be unique in a dictionary
We cannot have a sequence type as key

'''

my_dict1 = {}
print(type(my_dict1))

mydict2 = {'Name':['Yashwanth','Person A','Person B'],'Reg No.':[1043,4012,5624],'Degree':['Mtech','Btech','ATech']}
print(mydict2.keys())
print(mydict2.values())

print(mydict2['Name']) # Printing Values by Keys

# Adding a Key Value pair in a existing Dictionary
mydict2['Key'] = 'YouTube'
print(mydict2)

# Updating - same function as Adding
mydict2.update({"Mahindra":['Vinayak','Maharaj']})
print(mydict2)

# Removing Elements
# pop
mydict2.pop("Mahindra")  # Takes in Key and deletes the value
print(mydict2)

# pop_item - Will AUTOMATICALLY Remove the last added key value pari
mydict2.popitem()
print(mydict2)