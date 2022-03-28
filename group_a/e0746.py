class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = 0, 0
        
        for val in cost:
            curr = min(prev2, prev1) + val
            prev2 = prev1
            prev1 = curr
            
        return min(prev2, prev1)
