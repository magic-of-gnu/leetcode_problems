

class Solution:
    def minPathSum(self, grid):

        def dfs(grid, ii, jj, current_sum, memo):

            # print()
            # print(f'ii: {ii} jj: {jj}')
        
            if (ii == m and jj < n) or (ii < m and jj == n):
                # print(f'exiting ii: {ii} jj: {jj}')
                return None
        
        
            if (ii, jj) in memo:
                return memo[(ii,jj)]

            current_sum += grid[ii][jj]
        
            v1 = dfs(grid, ii+1, jj  , current_sum, memo)
            v2 = dfs(grid, ii  , jj+1, current_sum, memo)
        
            current_min = memo.get((ii,jj), current_sum)
            vals = []
        
            if v1 is not None:
                vals.append(v1)
            if v2 is not None:
                vals.append(v2)

            # print(f'ii: {ii} jj: {jj} vals: {vals}')

            if not vals:
                # exiting condition
                # print(f'end condition ii: {ii} jj: {jj}')
                children_min_value = grid[ii][jj]
            else:
                children_min_value = min(vals) + grid[ii][jj]
        
            memo[(ii,jj)] = children_min_value
        
            return children_min_value

        m, n = len(grid), len(grid[0])

        memo = dict()
        dfs(grid, 0, 0, 0, memo)

        return memo[(0,0)]


    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [0] + [101] * (m-1)

        for ii in range(n):
            dp[0] = dp[0] + grid[ii][0]
            for jj in range(1, m):
                dp[jj] = min(dp[jj-1], dp[jj]) + grid[ii][jj]

        return dp[-1]


if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6]]
    output = 12

    grid = [
        [9,9,0,8,9,0,5,7,2,2,7,0,8,0,2,4,8],
        [4,4,2,7,6,0,9,7,3,2,5,4,6,5,4,8,7],
        [4,9,7,0,7,9,2,4,0,2,4,4,6,2,8,0,7],
        [7,7,9,6,6,4,8,4,8,7,9,4,7,6,9,6,5],
        [1,3,7,5,7,9,7,3,3,3,8,3,6,5,0,3,6],
        [7,1,0,7,5,0,6,6,5,3,2,6,0,0,9,5,7],
        [6,5,6,3,8,1,8,6,4,4,3,4,9,9,3,3,1],
        [1,0,2,9,7,9,3,1,7,5,1,8,2,8,4,7,6],
        [9,6,7,7,4,1,4,0,6,5,1,9,0,3,2,1,7],
        [2,0,8,7,1,7,4,3,5,6,1,9,4,0,0,2,7],
        [9,8,1,3,8,7,1,2,8,3,7,3,4,6,7,6,6],
        [4,8,3,8,1,0,4,4,1,0,4,1,4,4,0,3,5],
        [6,3,4,7,5,4,2,2,7,9,8,4,5,6,0,3,9],
        [0,4,9,7,1,0,7,7,3,2,1,4,7,6,0,0,0]
    ]

    sol = Solution()
    print(sol.minPathSum(grid))
