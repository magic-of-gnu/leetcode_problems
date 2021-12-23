# 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

# Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.


class Solution:
    def maxSideLength(self, mat, threshold):

        def binary_search(prefix_sum, ii, jj, k, threshold):
            # apply binary search on items
            '''

            Args:
                prefix_sum (list(list(int))): prefix sum
                ii, jj (int, int): location of base element
                k (int): length of the side
                threshold (int): some threshold for the sum
            '''

            low = 0
            high = k
            mid = low + (high-low) // 2

            _low, _mid, _high = low, mid, high
            print(prefix_sum)
            print(f'ii: {ii} jj: {jj} k: {k}')

            while True:

                print()
                print(f'_low: {_low} _mid: {_mid} _high: {_high}')
                print(f'low: {low} mid: {mid} high: {high}')

                if low == mid == high:
                    break

                if mid < low:
                    break

                if high < mid:
                    break

                low, mid, high = _low, _mid, _high
                print(f's: {s}')
                s = prefix_sum[ii+_mid][jj+_mid] - prefix_sum[ii][jj]
                print((ii, jj), (ii+_mid, jj+_mid))

                # 0    10      thresh    100
                if s < threshold:
                    _low = _mid + 1
                elif s > threshold:
                    _high = _mid - 1
                else: # s == threshold:
                    break

                _mid = _low + (_high-_low) // 2

            return _mid + 1 # length


        m, n = len(mat), len(mat[0])
        max_length = 0

        prefix_sum = [[0 for jj in range(n)] for ii in range(m)]

        for ii in range(m):
            s = 0

            for jj in range(n):
                s += mat[ii][jj]

                if ii == 0:
                    prefix_sum[ii][jj] = s
                else:
                    prefix_sum[ii][jj] = prefix_sum[ii-1][jj] + s

        k = min(m, n) - 1
        print(f'k: {k}')
        for ii in range(n):
            for jj in range(m):
                k = min(m-ii, n-jj) - 1
                if k <= 0:
                    continue
                length = binary_search(prefix_sum, ii, jj, k, threshold)
                max_length = max(max_length, length)



        # import pdb; pdb.set_trace()

        return max_length

if __name__ == "__main__":
     mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]; threshold = 4

     mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
     threshold = 6
     Output = 3

     # mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
     # threshold = 4
     # Output = 2

     # mat = [[20,3,54,30,60,53],[98,14,10,42,55,23],[90,79,46,21,43,78],[82,73,85,99,40,93],[11,57,0,26,39,37],[48,82,46,32,66,89],[30,55,92,81,50,41],[34,87,56,63,3,4]]
     # threshold = 92206

     # mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
     # threshold = 40184
     # Output = 2

     sol = Solution()
     print(sol.maxSideLength(mat, threshold))
