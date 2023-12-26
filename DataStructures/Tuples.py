# Creating an empty Tuple
# from typing_extensions import TypeVarTuple


Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)
 
# Creating a Tuple
# with the use of string
Tuple1 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple1)
 
# Creating a Tuple with
# the use of list
list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
 
# Creating a Tuple
# with the use of built-in function
Tuple1 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

# Accessing tuple
print(Tuple1[0])

# Unpacking the tuple
tuple2 = (37, "Umesh")
age, name = tuple2
print(str(age) + ' ' + name)