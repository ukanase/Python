class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
            - palindrome abca aaaac, acaac
            - edge case: string is already a palindrome
            - BF: 
                - O(n^2)
            - DC:
                - abbca daab   aaaab
                - if s[l] == s[r]
                    l++
                    r--
                  else if s[l] == s[r-1] and l <= (r-1)
                    charDel++
                    l++
                    r -= 2
                  else if s[l+1] == s[r] and l+1 <= r
                    charDel++
                    l += 2
                    r--
                  else 
                    return false
                    
                  if(charDel > 1)
                    return false
                  
        '''
        def isPalindrome(s: str, st: int, end: int) -> bool:            
            if st > end:
                return False
            
            while st <= end:
                if s[st] != s[end]:
                    return False
                st += 1
                end -= 1
            
            return True
                
        n = len(s)
        if n == 0:
            return True        
        l = 0
        r = n - 1
        delCount = 0
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue        
            
            return isPalindrome(s, l, r - 1) or isPalindrome(s, l+1, r)
            
        return True
    
s = Solution()
r = s.validPalindrome("ececabbacec")
print(r)