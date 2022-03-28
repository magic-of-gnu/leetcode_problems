class Solution:
    def minimumTotal(self, triangle) -> int:

        M = len(triangle)

        sums = [0]*M
        sums[0] = triangle[0][0]   # [1,0,0,0]
        # 1 0      # 0 0
        # 2 3      # 1 1
        # 4 5 6
        # 7 8 0 9
        # 8

        for ii in range(1,M):   # 1
            # sums = [7,8,10,0]
            next_sums = [0]*M   # [0,0,0,0]
            next_sums[0] = sums[0] + triangle[ii][0]  # [14,0,0,0]
            # sums =      [ 7,  8, 10, 0]
            # next_sums = [14, 13,  8, 0]
            for jj in range(1,len(row)):   # 1 till 4 (excl) 1, 2, 3
                # jj = 1   1                0         1              8
                # jj = 2   2                1         2              8
                next_sums[jj] = min(sums[jj-1], sums[jj]) + triangle[ii][jj] 

            next_sums[jj] = sums[jj-1] + triangle[ii][jj]  # sums[1] + 6

            sums = next_sums  

        return min(sums)


    def minimumTotal(self, triangle) -> int:

        # M = 4
        # 0 1 2 3
        # 1 0         # 0
        # 2 3         # 1
        # 4 5 6       # 2 ii = 2
        # 7 8 0 9     # 3       

        M = len(triangle)

        for ii in reversed(range(M-1)):
            for jj in range(ii+1):   # 1 till 4 (excl) 1, 2, 3
                triangle[ii][jj] = min(triangle[ii+1][jj], triangle[ii+1][jj+1]) + triangle[ii][jj]
                

        return triangle[0][0]



if __name__ == "__main__":
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

    sol = Solution()
    print(sol.minimumTotal(triangle))

    pass
