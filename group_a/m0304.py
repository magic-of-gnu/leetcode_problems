from pprint import pprint as pp


class NumMatrix:

    def __init__(self, matrix):
        self.mat = matrix
        self.nrows = len(matrix)
        self.ncols = len(matrix[0])

        self.prefix_mat = self.create_prefix_mat(self.mat, self.nrows, self.ncols)
        pp(self.prefix_mat)


    def create_prefix_mat(self, mat, nrows, ncols):
        # first row
        prefix_mat = [[0] * (ncols+1) for _ in range(nrows+1)]
        prefix_sum = 0

        for jj in range(1, ncols+1):
            prefix_sum += mat[0][jj-1]
            prefix_mat[1][jj] = prefix_sum

        for ii in range(2, nrows+1):
            sum_current_row = 0
            for jj in range(1, ncols+1):
                prefix_mat[ii][jj] = sum_current_row + prefix_mat[ii-1][jj] + mat[ii-1][jj-1]
                sum_current_row += mat[ii-1][jj-1]

        return prefix_mat

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = self.prefix_mat[row2+1][col2+1]
        sqr = self.prefix_mat[row2+1][col1]
        sqc = self.prefix_mat[row1][col2+1]
        intersection = self.prefix_mat[row1][col1]

        print(total, sqr, sqc, intersection)

        return total - sqr - sqc + intersection
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



if __name__ == "__main__":

    commands = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    regions = [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    output = [None, 8, 11, 12]

    sol = NumMatrix(matrix)
    print(sol.sumRegion(*regions[0]))
