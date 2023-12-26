#
# Complete the mergeArrays function below.
#
from heapq import heapify, heappush, heappop, heappushpop
def mergeArrays(arr):
    '''
        - identify sort order of input
            - loop through each array in arr from 1 to n-1
            - if nums[i] != nums[i-1] 
                isAsc = nums[i] > nums[i-1]
        BF:
            - merge all and sort
            - nk * log (nk)
        Using MinHEap:
            - add all arrays to minHeap prioritize by current index value
                - [val, index, list]
            - TC: O(nk * log(k))
            - SC: O(nk) +  O(k)
    '''
    #
    k = len(arr)
    # isAsc = False
    sortOrderFound = False
    for i in range(k):
        curList = arr[i]
        curLen = len(curList)
        for j in range(1, curLen):
            if curList[j] != curList[j-1] :
                isAsc = curList[j] > curList[j-1]
                sortOrderFound = True
                break
        
        if sortOrderFound :
            print(f"Sort order {isAsc}")
            dir = 1 if isAsc else -1
            break       
    
    heap = []
    # insert first element of each list to heap
    for i in range(k):
        curList = arr[i]
        heappush(heap, [dir * curList[0], 0, curList])
        # if isAsc :
        #     # if ascending order create minHeap else maxHeap
        #     heappush(heap, [curList[0], 0, curList])
        # else: 
        #     heappush(heap, [-curList[0], 0, curList])
            
    result = []
    while heap:
        val, curIndex, curList = heappop(heap)
        result.append(dir * val)
        # if isAsc :
        #     result.append(val)
        # else:
        #     result.append(-val)
        # if list contains more elements
        if curIndex < len(curList) - 1 :
            nextIndex = curIndex + 1
            heappush(heap, [dir * curList[nextIndex], nextIndex, curList])
            # if isAsc :
            #     heappush(heap, [curList[nextIndex], nextIndex, curList])
            # else: 
            #     heappush(heap, [-curList[nextIndex], nextIndex, curList])
    
    return result


# input = [[1, 20, 30, 40],[2, 3, 21, 34,],[12, 34, 59]]
# edge case
# input = [[1, 1, 1, 1],[1, 1, 1, 1,],[1, 1, 2]]
input = [[1],[1, 1, 1, 1,],[1, 1, -2]]
# input = [[1, 5, 40],[1, 1, 1, 1,],[-6, -5, -4]]
res = mergeArrays(input)
print(res)
                