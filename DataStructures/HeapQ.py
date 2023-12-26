# Python code to demonstrate working of 
# heapify(), heappush() and heappop()
  
# importing "heapq" to implement heap queue
import heapq
  
# initializing list
li = [5, 7, 9, 1, 3]
  
# using heapify to convert list into heap
heapq.heapify(li)
  
# printing created heap
print ("The created heap is : ",end="")
print (list(li))
  
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
  
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))
  
# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))
# pop removes last element from the list
# print (li.pop())

# max heap
print(li)
maxHeap = []
heapq.heapify(maxHeap)
for val in li :
    heapq.heappush(maxHeap, -val)
        
print('maxValue ' + str(-maxHeap[0]))

# employee 
from heapq import heappush, heappop

class Employee:
    noOfObjects=0
    def __init__(self,name:str,age:int) -> None:
        self.name=name
        self.age=age
        # Employee.noOfObjects+=1
    
    # forward declaration for other
    def __lt__(self, other:"Employee") -> int:
        return self.age < other.age

umesh=Employee('umesh',23)
peru=Employee('Peru',23)
pq=[]
# heappush(pq,[peru.age,peru])
# heappush(pq,[umesh.age,umesh])
heappush(pq,(peru))
heappush(pq,(umesh))
while pq:
    obj=heappop(pq)
    print(obj.name,obj.age)
    print(f'{obj.name} age is {obj.age}')