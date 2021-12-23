class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
                       
        dp = [0] * m
        dp[-1] = max(1-grid[-1][-1], 1)
        for jj in reversed(range(m-1)):
            dp[jj] = max(dp[jj+1]-grid[-1][jj], 1)
        
        for ii in reversed(range(n-1)):
            dp[-1] = max(dp[-1]-grid[ii][-1], 1)
                
            for jj in reversed(range(m-1)):
                
                dp[jj] = min(max(dp[jj+1] - grid[ii][jj], 1),
                             max(dp[jj]   - grid[ii][jj], 1)
                         )
                
        return dp[0]
                         
                         
if __name__ == "__main__":
    dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

    sol = Solution()
    print(sol.calculateMinimumHP(dungeon))
