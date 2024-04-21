
def minOperations( boxes):
    """
    :type boxes: str
    :rtype: List[int]        
    BF: O(n^2)
        for i=0 to n-1
            minOps = 0 
            for j = 0 to n-1

    I: O(n)
        left to right
        all boxes i
        0 1 3
        right to left
        1 0 0
        1 1 3        
    """
    n = len(boxes)
    leftScore = [0]*n
    rightScore = [0]*n
            
    boxesSeen = 1 if boxes[0] == '1' else 0
    for i in range(1, n):
        leftScore[i] = leftScore[i-1] + boxesSeen
        if boxes[i] == '1':
            boxesSeen += 1                 
    
    boxesSeen = 1 if boxes[n-1] == '1' else 0
    for i in range(n-2, -1, -1):
        rightScore[i] = rightScore[i+1] + boxesSeen
        if boxes[i] == '1':
            boxesSeen += 1 
    
    result = [0]*n
    for i in range(n):
        result[i] = leftScore[i] + rightScore[i]
    
    return result


s = '001011'
r = minOperations(s)
print(r)



    
    