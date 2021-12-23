# 1905. Count Sub Islands

# https://leetcode.com/problems/count-sub-islands/

from collections import deque

class Solution:
    # def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    def countSubIslands(self, grid, grid2):

        n, m = len(grid), len(grid[0])

        def check_value(ii, jj, queue):
            if ii < 0 or ii >= n or jj < 0 or jj >= m: # if outside of grid
                return True

            if grid[ii][jj] == 4:   # if seen
                return None

            if grid[ii][jj] == 3:   # if land in grid1 and land in grid2
                grid[ii][jj] = 4
                queue.append((ii,jj))
                return True

            if grid[ii][jj] % 2 == 0: # if land in grid1 and water in grid2 or water in both grids
                return True

            return False

        def check_neighbors(ii, jj, queue):
            is_valid = True
            for item in [(-1,0), (0,1), (1,0), (0,-1)]:
                a = check_value(ii+item[0], jj+item[1], queue)
                if a is not None:
                    is_valid = is_valid & a

            # return children, is_valid
            return is_valid

        def dfs(ii, jj):
            if grid[ii][jj] == 4:
                return False
            elif grid[ii][jj] != 3:
                return False

            is_valid = True
            queue = deque([(ii, jj)])
            while queue:
                ii, jj = queue.pop()
                valid = check_neighbors(ii, jj, queue)
                is_valid = is_valid & valid

            return is_valid

        for ii in range(n):
            for jj in range(m):
                grid[ii][jj] *= 2
                grid[ii][jj] += grid2[ii][jj]

        count = 0
        for ii in range(n):
            for jj in range(m):
                count += dfs(ii, jj)

        return count


if __name__ == "__main__":
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]

    grid1 = [
             [1,0,1,0,1,1,1,0,1,1,0,1,1,1,1],
             [1,1,1,1,1,0,1,1,1,1,0,0,0,1,1],
             [1,1,1,1,1,0,1,1,1,1,1,1,1,1,0],
             [1,1,1,1,0,1,0,0,1,1,1,1,0,0,1],
             [0,0,1,1,1,1,1,0,1,0,1,1,1,0,0],
             [0,1,1,1,1,1,1,1,1,0,1,1,1,1,1],
             [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [1,1,1,1,0,1,0,0,1,1,1,0,0,1,1],
             [1,0,1,1,1,1,1,0,0,1,1,1,1,0,1],
             [0,1,0,0,0,1,1,1,1,1,1,1,0,0,1],
    ]
    grid2 = [[1,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
             [1,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
             [1,1,1,0,1,1,1,1,1,1,0,1,0,1,1],
             [1,0,0,1,0,1,1,1,0,0,1,0,1,0,1],
             [0,1,1,1,1,1,1,0,1,1,1,1,1,0,0],
             [0,1,1,1,1,1,1,1,1,1,0,1,1,1,0],
             [1,1,1,1,1,1,1,1,1,0,0,1,0,1,1],
             [1,0,1,0,0,1,1,1,0,1,0,1,1,1,1],
             [0,1,0,1,1,1,0,1,1,1,1,0,0,0,1],
             [1,1,1,0,1,0,0,0,1,1,0,0,1,1,1],
             [1,0,0,1,1,1,0,0,0,0,1,0,1,0,0],
             [0,0,1,1,1,1,1,0,1,0,1,1,1,0,0]
    ]
    Output = 6

    ggg = [  [3,0,3,0,2,2,3,0,2,2,0,2,3,2,3],
             [3,3,2,3,2,1,3,3,3,3,0,1,0,3,3],
             [3,3,3,2,3,1,3,3,3,3,2,3,2,3,1],
             [3,2,2,3,0,3,1,1,2,2,3,2,1,0,3],
             [0,1,3,3,3,3,3,0,3,1,3,3,3,0,0],
             [0,3,3,3,3,3,3,3,3,1,2,3,3,3,2],
             [1,1,3,3,3,3,3,3,3,2,2,3,2,3,1],
             [1,2,3,2,2,3,3,3,0,3,2,3,3,3,3],
             [2,3,2,3,3,3,2,3,3,3,3,2,2,2,1],
             [3,3,3,2,1,2,0,0,3,3,2,0,1,3,3],
             [3,0,2,3,3,3,2,0,0,2,3,2,3,0,2],
             [0,2,1,1,1,3,3,2,3,2,3,3,1,0,2]
    ]

    sol = Solution()
    print(sol.countSubIslands(grid1, grid2))
