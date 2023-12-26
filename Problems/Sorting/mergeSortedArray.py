from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        k = len(nums1) - 1
        i = m - 1
        j = n - 1
        
        while (i >= 0 and j >= 0):
            
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]                
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            
        while i >= 0 :
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        
        # not needed            
        # while j >= 0 :
        #     nums1[k] = nums2[j]
        #     j -= 1
        #     k -= 1
            
        return nums1
    

s = Solution()
nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6]
n = 3
r = s.merge(nums1, m, nums2, 3)
print(r)
        