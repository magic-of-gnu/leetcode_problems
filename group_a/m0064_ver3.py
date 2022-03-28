class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [grid[0][0]]
        
        for ind, val in enumerate(grid[0][1:], start=1):
            dp.append(val+dp[-1])
            
        for row in grid[1:]:
            dp[0] = dp[0]+row[0]
            for ind, val in enumerate(row[1:], start=1):
                dp[ind] = min(dp[ind-1], dp[ind]) + val
                
        return dp[-1]
