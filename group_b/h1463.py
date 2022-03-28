class Solution:
    def cherryPickup(self, grid):

        m, n = len(grid), len(grid[0])

        dp = [[[0 for kk in range(n)] for jj in range(n)] for ii in range(m)]

        for ii in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    result = grid[ii][col1]

                    if col1 != col2:
                        result += grid[ii][col2]

                    if ii != m - 1: # if not last
                        result += max([dp[ii+1][c1][c2] 
                                      for c1 in range(max(0, col1-1), min(n-1, col1+1)+1)
                                      for c2 in range(max(0, col2-1), min(n-1, col2+1)+1)
                                      ])

                    dp[ii][col1][col2] = result

        return dp[0][0][n-1]


    def cherryPickup(self, grid):

        m, n = len(grid), len(grid[0])
        memo = dict()

        def dp(grid, memo, ii, col1, col2):

            if (ii, col1, col2) in memo:
                return memo[(ii, col1, col2)]

            result = grid[ii][col1]

            if col1 != col2:
                result += grid[ii][col2]

            if ii == m - 1:
                return result

            result += max([dp(grid,memo,ii+1,c1,c2)
                          for c1 in range(max(0, col1-1), min(n-1, col1+1)+1)
                          for c2 in range(max(0, col2-1), min(n-1, col2+1)+1)
                         ])

            memo[(ii,col1,col2)] = result
            return memo[(ii,col1,col2)]

        dp(grid, memo, 0, 0, n-1)

        return memo[(0,0,n-1)]


if __name__ == "__main__":
    grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]

    sol = Solution()
    print(sol.cherryPickup(grid))
