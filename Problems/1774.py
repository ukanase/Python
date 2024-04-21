class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        0 or more toppings
        atmost 2 of each type topping
        n - baseCosts
        m - toppingCosts
        BF: recursion TC = O(n*3^m)
            - branching factor 3 to the power of height of recursion tree
            foreach base in baseCosts
                desertCost = baseCost
                foreach toping in topingCosts
                    if desertCost + toping <= target:
                        // try adding one more time same toping
            
        """
        def getClosestCostForBase(toppingCosts, i, target, dic):
            if i == len(toppingCosts):
                return 0
            
            if (i, target) in dic:
                return dic[(i, target)]
            
            result = 0
            prevResultAbsDiff = abs(target - result)
            for j in range(2):
                curToppingCost = j * toppingCosts[i]
                newTarget = target - curToppingCost
                newResult = getClosestCostForBase(toppingCosts, i+1, newTarget, dic)
                newResultAbsDiff = abs(target - newResult)
                if newResultAbsDiff < prevResultAbsDiff:
                    result = newResult
            
            dic[(i, target)] = result
            return dic[(i, target)]             
        
        result = baseCosts[0]
        prevResultAbsDiff = abs(target - result)
        dic = {}      
        for base in baseCosts:
            newTargetWithCurBase = target - base
            newResult = base + getClosestCostForBase(toppingCosts, 0, newTargetWithCurBase, dic)
            newResultAbsDiff = abs(target, newResult)
            if newResultAbsDiff < prevResultAbsDiff:
                result = newResult
                prevResultAbsDiff = newResultAbsDiff
        
        # print(dic)
        return result

"""
    baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
    base = 2
    f(topping, 0, 16)
        f(1, 16)
            f(2, 16)
                f(3, 16) -> 0
                5 + f(3, 11) -> 5
                10 + f(3, 6) -> 10
     baseCosts = [3,10], toppingCosts = [2,5], target = 9                
"""
s = Solution()
baseCosts = [4]
toppingCosts = [9]
target = 9
r = s.closestCost(baseCosts, toppingCosts, target)
print(r)
