# 1878. Get Biggest Three Rhombus Sums in a Grid

class Solution:
    def getBiggestThree(self, grid):
        
        def update_results(sums, s, min_sum):
            if not(s > min_sum):
                return sums, min_sum

            if sums.get(s, None) is None:
                sums[s] = 1
            else:
                return sums, min_sum

            _sorted = sorted(sums.keys())[-3:]
            sums = {key: 1 for key in _sorted}
            min_sum = _sorted[0]

            return sums, min_sum

        m, n = len(grid), len(grid[0])

        sums = {-1:1}
        min_sum =-1 

        for ii in range(m):
            for jj in range(n):
                sums, min_sum = update_results(sums, grid[ii][jj], min_sum)

                d = 1
                while True:
                    s = 0
                    if not(ii - d >= 0 and ii + d < m and jj - d >= 0 and jj + d < n):
                        break

                    for di in range(1, d+1):
                        if di == d:
                            s += grid[ii-di][jj] + grid[ii+di][jj]
                            s += grid[ii][jj-di] + grid[ii][jj+di]
                        else:
                            ki = d-di
                            s += grid[ii-di][jj-ki] + grid[ii-di][jj+ki]
                            s += grid[ii+di][jj-ki] + grid[ii+di][jj+ki]

                    sums, min_sum = update_results(sums, s, min_sum)
                    d += 1

        if sums.get(-1):
            sums.pop(-1)
        return list(reversed(sums.keys()))

if __name__ == "__main__":
    grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
    grid = [[300,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]

    grid = [[20,17,9,13,5,2,9,1,5],[14,9,9,9,16,18,3,4,12],[18,15,10,20,19,20,15,12,11],[19,16,19,18,8,13,15,14,11],[4,19,5,2,19,17,7,2,2]]

    sol = Solution()
    print(sol.getBiggestThree(grid))
