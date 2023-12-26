class TreeNode():
   def __init__(self, val=None, left_ptr=None, right_ptr=None, next_right=None):
       self.val = val
       self.left_ptr = left_ptr
       self.right_ptr = right_ptr
       self.next_right = next_right

# complete the function below

from typing import Deque
# from collections import deque

def populateSiblingPointers(root):
    
    if root == None:
        return None
    
    queue = Deque[TreeNode]()
    queue.append(root)
    
    while queue:
        
        count = len(queue)
        prev:TreeNode = None
        for i in range(count):
            cur = queue.popleft()
            
            if cur.left_ptr :
                queue.append(cur.left_ptr)
                
            if cur.right_ptr :
                queue.append(cur.right_ptr)
            
            if prev :
                prev.next_right = cur
            
            prev = cur
    
    return root

                