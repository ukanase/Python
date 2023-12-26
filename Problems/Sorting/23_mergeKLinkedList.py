# Definition for singly-linked list.

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from heapq import heapify, heappush, heappop, heappushpop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
            - input is in asc order so minHeap required
                - (val, curNode)
            - 
        '''
        class PQNode:
            def __init__(self, node:ListNode) -> None:
                self.node = node
            
            # use forward declaration i.e. "ClassName" 
            def __lt__(self, other:"PQNode") -> int:
                return self.node.val < other.node.val
        
        # minHeap = []
        minHeap = []       
        for linkedList in lists:
            if linkedList != None :
                heappush(minHeap, (PQNode(linkedList)))
            
        sentinel = ListNode()    
        cur = sentinel
        while minHeap:
            pqNode = heappop(minHeap)
            curNode = pqNode.node
            cur.next = curNode
            if curNode.next != None :
                nextNode = curNode.next
                heappush(minHeap, (PQNode(nextNode)))
            else:
                heappop(minHeap)
            curNode.next = None
            cur = cur.next
        
        return sentinel.next
    
'''
[[1,2,2],[1,1,2]]
2, 4
sentinel - 1 -> 2 -> 3 -> 4 -> 6 -> 7
'''
list1  = ListNode(10)
list2 = ListNode(10)
lists = [list1, list2]
s = Solution()
r =  s.mergeKLists(lists)

cur = r
while cur :
    print(cur.val)
    cur = cur.next


        
        