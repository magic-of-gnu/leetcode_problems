# Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        num_states = 2
        m, n = len(grid), len(grid[0])

        def dfs(grid, queue):
            if not queue:
                return
            new_queue = []

            for ii, jj in queue:
                # ii, jj = q
                if ii - 1 >= 0 and grid[ii-1][jj] < num_states and grid[ii-1][jj] % num_states == 1:
                    grid[ii-1][jj] += num_states
                    new_queue.append((ii-1, jj))

                if jj - 1 >= 0 and grid[ii][jj-1] < num_states and grid[ii][jj-1] % num_states == 1:
                    grid[ii][jj-1] += num_states
                    new_queue.append((ii, jj-1))

                if ii + 1 < m and grid[ii+1][jj] < num_states and grid[ii+1][jj] % num_states == 1:
                    grid[ii+1][jj] += num_states
                    new_queue.append((ii+1, jj))

                if jj + 1 < n and grid[ii][jj+1] < num_states and grid[ii][jj+1] % num_states == 1:
                    grid[ii][jj+1] += num_states
                    new_queue.append((ii, jj+1))

            dfs(grid, new_queue)

        num_islands = 0

        for ii in range(m):
            for jj in range(n):
                grid[ii][jj] = int(grid[ii][jj])

        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] < num_states and grid[ii][jj] == 1:
                    num_islands += 1
                    dfs(grid, [(ii,jj)])

        return num_islands
                    


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "1"],
            ["0", "1", "0", "1", "0"],
            ["0", "0", "0", "0", "0"],
            ["1", "1", "0", "1", "1"],
            ["0", "1", "1", "1", "0"]
           ]

    Output = 2

    grid =[ ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
          ]


    sol = Solution()
    print(sol.numIslands(grid))


