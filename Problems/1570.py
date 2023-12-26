from typing import List

class SparseVector:
    
    def __init__(self, nums: List[int]):
        self.vector = []
        for i, val in enumerate(nums):
            if val != 0 :
                self.vector.append((i,val))
        
        print(self.vector)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        '''
            - nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
            - sparsevestor1 - [(1,0), (2,3), (3, 4)]
            - sparsevector2 - [(3,1), (4,3)]
            - i = 0 j = 0
            result = 0
            - while i < len(sv1) and j < len(sv2)
                    sv1Val, sv1Index = sv1[i]
                    sv2Val, sv2Index = sv2[j]
                    
        '''
        result = 0
        i, j = 0, 0        
        while i < len(self.vector) and j < len(vec.vector):
            vec1Index, vec1Val = self.vector[i]
            vec2Index, vec2Val = vec.vector[j]
            
            if vec1Index == vec2Index:
                result += vec1Val * vec2Val
                i += 1 
                j += 1            
            elif vec1Index < vec2Index:
                i += 1
            else:
                j += 1
        
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
r = v1.dotProduct(v2)
print(r)