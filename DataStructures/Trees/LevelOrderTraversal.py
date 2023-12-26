# Definition for a binary tree node.
from typing import List, Optional, Deque
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # edge case 
        if root == None:
            return []
        
        result = []
        queue = Deque[TreeNode]()
        queue.append(root)
        
        while queue:
            
            count = len(queue)
            level = []
            for i in range(count):
                cur = queue.popleft()
                level.append(cur.val)
                
                if cur.left != None : 
                    queue.append(cur.left)
                
                if cur.right != None :
                    queue.append(cur.right)
            
            result.append(level)
    
        return result

        