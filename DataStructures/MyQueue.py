# Enqueue, Dequeue, IsEmpty, Count

from collections  import deque
import queue as pyQ
    
class QueueUsingDeque:
    
    def __init__(self) -> None:
        self.queue = deque()
        
    def Enqueue(self, value: int) -> None:
        self.queue.append(value)
        
    def Dequeue(self) -> int:
        if len(self.queue) == 0 : 
            raise IndexError("Queue is empty")
        # popleft is for removing elements from front
        # pop is for removing elements from back - stack
        return self.queue.popleft()
    
    def IsEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else :
            return False
        
class QueueUsingQueue:
    
    def  __init__(self) -> None:
        self.queue = pyQ.SimpleQueue()
        
    def Enqueue(self, value: int) -> None:
        self.queue.put(value)
        
    def Dequeue(self) -> int:
        if self.queue.empty():
            raise IndexError("Queue is empty")
        return self.queue.get()
        # if len(self.queue.) == 0 : 
        #     raise IndexError("Queue is empty")
        # # popleft is for removing elements from front
        # # pop is for removing elements from back
        # return self.queue.popleft()
    
    def IsEmpty(self) -> bool:
        return self.queue.empty()
        # if len(self.queue) == 0:
        #     return True
        # else :
        #     return False