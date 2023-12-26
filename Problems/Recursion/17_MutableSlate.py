
from typing import List
from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
            - generate strings with all the possible letters for an int
            - dic => {2 to 9 with letters}
            - TC => internal nodes + leaf nodes
                 => 4^n + (4^n) * n
                 => O(n * 4^n)
            - SC => input + aux space + output 
                 => O(n) + O(n) + 4^n => O(4^n)
        '''
        # dic:defaultdict(lambda: []) = {
        #     '2': ['a', 'b', 'c'],
        #     '3': ['d', 'e', 'f'],
        #     '4': ['g', 'h', 'i'],
        #     '5': ['j', 'k', 'l'],
        #     '6': ['m', 'n', 'o'],
        #     '7': ['p', 'q', 'r', 's'],
        #     '8': ['t', 'u', 'v'],
        #     '9': ['w', 'x', 'y', 'z'] }
        
        result = []
        dic = defaultdict(lambda: [""])
        dic['2'] = ['a', 'b', 'c']
        dic['3'] = ['d', 'e', 'f']
        dic['4'] = ['g', 'h', 'i']
        dic['5'] = ['j', 'k', 'l']
        dic['6'] = ['m', 'n', 'o']
        dic['7'] = ['p', 'q', 'r', 's']
        dic['8'] = ['t', 'u', 'v']
        dic['9'] = ['w', 'x', 'y', 'z'] 
        
        def helper(self, index:int, slate:List) -> None:
            # base case
            if index == len(digits):
                print(slate)
                result.append("".join(slate))
                return
                
            # recursion case
            for char in dic[digits[index]]:
                slate.append(char)
                helper(self, index + 1, slate)
                slate.pop()        

        helper(self, 0, [])           
        return result 


s = Solution()
r = s.letterCombinations("12")
print(r)
