from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
            BF
                - recursion
                - exponential
            DC:
                - lee(t(c)o)de)
                - keep open brackets in stack
                - foreach close bracket remove one open bracket from stack
                -   if st is empty
                        add close bracket index to deleted
                - at the end all open bracket indices from stack are to be deleted 
                - create result string excluding deleted indices
                - TC: O(n)
                - SC: O(n)
        '''
        opStack = deque()
        tobeDeleted = set()
        slist = list(s)
        # for char in s:
        # for i in range(len(s)):
        for i, char in enumerate(s):
            # char = s[i]
            if char == '(':
                opStack.append(i)
            elif char == ')':
                if len(opStack) == 0:
                    # no matching open bracket, mark ) bracket to be deleted
                    # tobeDeleted.add(i)
                    # delete ) from sList
                    slist[i] = ""
                else:
                    opStack.pop()
        
        while opStack:
            slist[opStack.pop()] = ""
        # add multiple at once
        # tobeDeleted.update(opStack)
        
        # result = []
        # # print(tobeDeleted)
        # for i in range(len(s)):
        #     if i not in tobeDeleted:
        #         result.append(s[i])
        
        return "".join(slist)
    
c = Solution()
r = c.minRemoveToMakeValid("((((a)((v)()()")
# r = c.minRemoveToMakeValid("(a)((v)")
print(r)

        
        