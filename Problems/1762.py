from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        '''
            - ocean view building 
                - all buildings to the right have less height
                   
                  0  1  2  3 
            - e.g 4, 2, 3, 1        => 
            BF: 
                - O(n^2)
            I: 
                - result: stack
                - max: heights[n-1], result = [heights[n-1]]
                - for i in n-2 to 0
                    if curHeight > max 
                        result.append(curHeight)
                        max = curHeight
        '''
        result = []
        n = len(heights)
        max = heights[n-1]
        result.append(n-1)
        
        for i in range(n-2, -1, -1):
            print(i)
            curHeight = heights[i]
            if curHeight > max:
                result.append(i)
                max = curHeight            
        
        return result[::-1]
    
s  = Solution()
r = s.findBuildings([4,2,3,1])
print(r)
