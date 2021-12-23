class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        
        # first row
        for jj in range(1,n):
            dp[jj] = dp[jj-1] + grid[0][jj]
            
        # remaining rows
        for ii in range(1, m):
            dp[0] = dp[0] + grid[ii][0]
            for jj in range(1, n):
                dp[jj] = min(dp[jj-1], dp[jj]) + grid[ii][jj]
                
        return dp[-1]
