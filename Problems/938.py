# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
            sum = 0
            
            helper(node)
                if node.val between low and high 
                    sum += node.val
                
                if node.left != None and node.val > low
                    helper(node.left)
                
                if node.right != None and node.val < high
                    helper(node.right)
                    
            
        '''
        result = [0]
        
        def helper(node: TreeNode) -> None:
            if low <= node.val and node.val <= high :
                # nonlocal result 
                result[0] += node.val

            if node.left != None and node.val > low :
                helper(node.left)

            if node.right != None and node.val < high : 
                helper(node.right)
        
        # sum = 0
        helper(root)
        
        return result[0]
        