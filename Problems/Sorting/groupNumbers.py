def groupNums(nums: list):
    
    def swap(nums: list, x: int, y: int) -> None :
        temp = nums[x]
        nums[x] = nums[y] 
        nums[y] = temp
        
    e = 0
    o = len(nums) - 1
    
    while e < o :
        if nums[e] % 2 != 0 :
            swap(nums, e, o)
            o -= 1
        else:
            e += 1
        
        # if nums[o] % 2 == 0:
        #     swap(nums, e, o)
        #     e += 1
        # else:
        #     o -= 1

nums = [1,2,3,4,5,6]
groupNums(nums)
print(nums)

def groupNumsOptimized(nums: list):
    
    e = -1
    for i in range(len(nums)):
        if nums[i] % 2 == 0 : 
            e += 1
            nums[e], nums[i] = nums[i], nums[e]
    
nums = [1,2,3,4,5,6]
groupNums(nums)
print(nums) 
     
