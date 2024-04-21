def sayHi() :
    return "Hi"

# global variables use
def f():
    global i
    i += 20
    print(i)

i = 10
f()

# every variable assigned to in function is local; unless explicitly marked as global or nonlocal
class Test:   
    a = 10
    b = 20    
    def getSum(self):        
        return Test.a + Test.b
    
    # closure example
    def getValue(self):
        val = 1985
        # reference variable
        arr = [10]
        
        def calcValue():
            nonlocal val
            # below line will give error if nonlocal is removed; use of unassigned local variable
            val += 10
            arr[0] += 10
        
        calcValue()
        print(f"value of val: {val}")
        return arr

t = Test()
print(t.getSum())
print(t.getValue())

# for with negative counting
# for i in range(4, -1, -1):
#     print(i)

if i == 10:
    print('Hi')
else:
    print('Bye')
    
    