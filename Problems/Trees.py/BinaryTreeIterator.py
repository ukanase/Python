class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr

# Complete the below functions

from typing import Deque

class BTIterator():
    def __init__(self, root = None):
        # initialize here
        # until left is null add all the left ptr to the stack
        self.stack = Deque[TreeNode]()
        temp:TreeNode = root
        
        while temp:
            self.stack.append(temp)
            temp = temp.left_ptr        

    def hasNext(self):
        # return true of stack is not empty
        return len(self.stack) > 0

    def next(self):
        # return node from top of stack
        cur = self.stack.pop()
        temp:TreeNode = cur.right_ptr
        # go to the right of current node and insert it to stack until left ptr is not null        
        while temp:
            self.stack.append(temp)
            temp = temp.left_ptr
        
        return cur.val

# stack -> 
# temp -> 2
# ouput -> 3, 1, 0, 4, 2, 5