class Solution:
    def spiralOrder(self, matrix):

        m, n = len(matrix), len(matrix[0])

        if m == 0 or n == 0:
            return matrix

        elif m == 1 or n == 1:
            return [matrix[ii][jj] for ii in range(m) for jj in range(n)]

        loops = 0
        ii, jj = 0, -1
        results = []
        direction = 1

        while True:

            for _ in range(n-loops):
                jj = jj + direction
                results.append(matrix[ii][jj])

            if len(results) == m*n:
                return results

            for _ in range(m-1-loops):
                ii = ii + direction
                results.append(matrix[ii][jj])

            if len(results) == m*n:
                return results

            loops += 1
            direction = -direction


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output = [1,2,3,6,9,8,7,4,5]

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output = [1,2,3,4,8,12,11,10,9,5,6,7]

    sol = Solution()
    print(sol.spiralOrder(matrix))

