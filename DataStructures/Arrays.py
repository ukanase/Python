# arrays are similar to list, only diff is they allow only single type of values
# importing "array" for array creations
import array as arr
 
# creating an array with integer type
# 'i' is type code for integer
a = arr.array('i', [1, 2, 3])
 
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# creating an array with float type
b = arr.array('d', [2.5, 3.2, 3.3])
 
# printing original array
print ("The new created array is : ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")
print()
    
for i, val in enumerate(b):
    print(f"index:{i} value:{val}", end=" ")    