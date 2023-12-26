
from typing import List


def mergeSort(nums: List[int]) :

    def helper(nums: list, st: int, end: int):

        # base case - leaf level worker case
        if st >= end:
            return

        # recursive case: internal node
        # mid = st + int((end - st)/2)
        mid = st + (end - st)//2
        helper(nums, st, mid)
        helper(nums, mid + 1, end)

        # merge sorted halfs
        aux = []
        i = st
        j = mid + 1
        while(i <= mid and j <= end):
            if (nums[i] <= nums[j]):   # to ensure stability of sort nums[i] <= nums[j]
                aux.append(nums[i])
                i += 1
            else:
                aux.append(nums[j])
                j += 1

        aux = aux + nums[i:mid+1]
        # while i <= mid:
        #     aux.append(nums[i])
        #     i += 1

        aux = aux + nums[j:end+1]
        # while j <= end:
        #     aux.append(nums[j])
        #     j += 1

        print(aux)
        nums[st:end+1] = aux
    
    n = len(nums)    
    helper(nums, 0, n - 1)

nums = [1, 4, 1, 2, 3]
mergeSort(nums)
print(nums)


def mergeSortOptimized(nums: list) :

    def helper(nums: list, st: int, end: int):

        # base case - leaf level worker case
        if st >= end:
            return

        # recursive case: internal node
        # mid = st + int((end - st)/2)
        mid = st + (end - st)//2
        helper(nums, st, mid)
        helper(nums, mid + 1, end)

        # merge sorted halfs
        # aux = []
        i = st
        j = mid + 1
        k = st
        while(i <= mid and j <= end):
            if (nums[i] <= nums[j]):   # to ensure stability of sort nums[i] <= nums[j]
                aux[k] = nums[i]
                i += 1                
            else:
                aux[k] = nums[j]
                j += 1
            k += 1
            
        while i <= mid:
            aux[k] = nums[i]
            i += 1
            k += 1

        while j <= end:
            aux[k] = nums[j]
            j += 1
            k += 1

        print(aux)
        nums[st:end+1] = aux[st:end+1]
    
    n = len(nums)
    aux = [-1]*n    
    helper(nums, 0, n - 1)

nums = [1, 4, 1, 2, 3]
mergeSortOptimized(nums)
print(nums)