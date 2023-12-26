# push, pop, peek, isEmpty

from collections import deque
import queue as pyQ

class MyStack:
    
    def __init__(self) -> None:
        self.stack = deque()
        
    def push(self, val: int) -> None:
        self.stack.append(val)

    def peek(self) -> int:
        if len(self.stack) == 0 : 
            raise IndexError("stack is empty")
        return self.stack[-1]
        
    def pop(self) -> int:
        if len(self.stack) == 0 : 
            raise IndexError("stack is empty")
        # pop can take index argument
        return self.stack.pop()
    
    def isEmpty(self) -> bool:
        return self.stack.count() == 0
    
    
class MyStackUsingLifoQueue:
    def __init__(self) -> None:
        self.stack = pyQ.LifoQueue()
        
    def push(self, val: int) -> None:
        self.stack.put(val)

    def peek(self) -> int:
        if self.stack.empty() : 
            raise IndexError("stack is empty")
        return self.stack[-1]
        
    def pop(self) -> int:
        if self.stack.empty() : 
            raise IndexError("stack is empty")
        # pop can take index argument
        return self.stack.get()
    
    def isEmpty(self) -> bool:
        return self.stack.empty()    