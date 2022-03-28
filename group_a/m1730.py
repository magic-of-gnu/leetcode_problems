class Solution:
    def getFood(self, grid):

        def find_starting_point(grid, char="*"):
            for ii in range(m):
                for jj in range(n):
                    if grid[ii][jj] == char:
                        return ii, jj

        def is_valid(grid,ii,jj,m,n,char='X'):
            if (not (0 <= ii < m and 0 <= jj < n)) or grid[ii][jj] == char:
                return False
            return True

        m, n = len(grid), len(grid[0])

        ii, jj = find_starting_point(grid)
        grid[ii][jj] = 'O'

        q = {(ii,jj):0}
        visited = dict()
        result = [float('inf')]

        while q:
            newq = dict()
            for state, num_steps in q.items():
                ii, jj = state # 1,2

                if (ii, jj) in visited:
                    continue

                visited[(ii,jj)] = 1

                if grid[ii][jj] == '#':
                    result[0] = min(result[0], num_steps)

                for (di, dj) in [(-1,0),(0,1),(1,0),(0,-1)]:
                    ni, nj = ii + di, jj + dj  # 0,2X ; 1,3 ; 2,2 ; 2,1V

                    if is_valid(grid, ni, nj, m, n):
                        newq[(ni,nj)] = min(newq.get((ni,nj), float('inf')), num_steps+1)


            q = newq

        return result[0] if result[0] != float('inf') else -1



if __name__ == "__main__":
    grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]

    sol = Solution()
    print(sol.getFood(grid))
