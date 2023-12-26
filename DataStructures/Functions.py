# Python program to illustrate
# *args for variable number of arguments

def myFun(*argv):
    for arg in argv:
        print(arg)
  
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# *kwargs for variable number of keyword arguments
 
 
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')

def evenOdd(x):
    """Function to check if the number is even or odd"""
     
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
 
# Driver code to call the function
print(evenOdd.__doc__)

# using lambda function
 
def cube(x): return x*x*x
 
cube_v2 = lambda x : x*x*x
 
print(cube(7))
print(cube_v2(7))
