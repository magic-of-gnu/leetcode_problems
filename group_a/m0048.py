from pprint import pprint as pp

class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def get_new_inds(i,j,n):
            return j    , n-1-i

        def get_new_inds_reversed(i,j,n):
            return n-1-j, i

        n = len(matrix)

        for ii in range(n//2):
            for jj in range(ii, n-ii-1):

                tmp = matrix[ii][jj]

                for _ in range(4):
                    newi, newj = get_new_inds(ii,jj,n)
                    newtmp = matrix[newi][newj]
                    matrix[newi][newj] = tmp
                    print(f'ii: {ii},{jj} -> {newi},{newj}')
                    print(f'tmp: {tmp} newtmp: {newtmp}')

                    ii, jj = newi, newj
                    tmp = newtmp


if __name__ == "__main__":
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    sol = Solution()
    pp(matrix)
    sol.rotate(matrix)
    pp(matrix)
        
