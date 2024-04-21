from collections import defaultdict

def maxLengthBetweenEqualCharacters(s):
    """
    :type s: str
    :rtype: int
    BF:
        O(n^2)
    I: O(n) ?
        first index of each character found
        result -1
        dic a 0 
        curIndex - dic[s[i]] - 1
    """
    dic = defaultdict(lambda: -1)
    result = -1
    n = len(s)
    for i in range(n):
        c = s[i]
        # if current char is not present in dic, add it with cur index       
        if dic[c] == -1:
            dic[c] = i           
        else:
            # sub str len abca 
            result = max(result, i - dic[c] - 1)
    
    return result

def maxLengthBetweenEqualCharacters_without_defaultdic(s):
    """
    :type s: str
    :rtype: int
    BF:
        O(n^2)
    I: O(n) ?
        first index of each character found
        result -1
        dic a 0 
        curIndex - dic[s[i]] - 1
    """
    dic = {}
    result = -1
    n = len(s)
    for i in range(n):
        c = s[i]
        # if current char is not present in dic, add it with cur index       
        if c in dic:
            # sub str len abca 
            result = max(result, i - dic[c] - 1)
        else:
            dic[c] = i           
    
    return result
            
    
    