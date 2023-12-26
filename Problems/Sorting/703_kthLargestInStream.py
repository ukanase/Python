import heapq
from typing import List

class KthLargest:
    
    # 1, 2, 3, 4, 5
    # minHeap of size k
    # init()
    #     - initialize minHeap
    #     - until heapSize > k  
    #         pop
    # add()
    # # edge case 
    # if (heapSize == k-1)
    #     heap.push(val)
    # else if val > heapTop 
    #   pop from heap
    #   push val
    #  
    # return heapTop

    def __init__(self, k: int, nums: List[int]):
        self._heap = nums
        self.k = k
        # initialize minHeap of size k
        heapq.heapify(self._heap)
        while len(self._heap) > k :
            heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        # 2, 3, 
        heapSize = len(self._heap)
        if heapSize == self.k - 1 :
            heapq.heappush(self._heap, val)
        # how to get smallest value from heap
        elif val > self._heap[0] :
            # heapq.heappop(self._heap)
            # heapq.heappush(self._heap, val)
            # Optimization using heappushpop
            heapq.heappushpop(self._heap, val)
                    
        return self._heap[0]        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)