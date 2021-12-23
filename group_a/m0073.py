class Solution:
    def setZeroes2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if not matrix:
            return
        
        rows, cols = set(), set()
        m, n = len(matrix), len(matrix[0])
        
        for ii in range(m):
            for jj in range(n):
                if matrix[ii][jj] == 0:
                    rows.add(ii)
                    cols.add(jj)
                    
        for r in rows:
            for jj in range(n):
                matrix[r][jj] = 0
                
        for c in cols:
            for ii in range(m):
                matrix[ii][c] = 0
                
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        zero_row, zero_col = False, False
        
        for ii in range(m):
            for jj in range(n):
                if matrix[ii][jj] == 0:
                    if ii == 0:
                        zero_row = True
                    if jj == 0:
                        zero_col = True

                    matrix[ii][ 0] = 0
                    matrix[ 0][jj] = 0
                    
        for ii in range(m-1,0,-1):
            if matrix[ii][0] == 0:
                for jj in range(n):
                    matrix[ii][jj] = 0
                    
        for jj in reversed(range(1,n)):
            if matrix[0][jj] == 0:
                for ii in range(m):
                    matrix[ii][jj] = 0
                    
        if zero_col is True:
            for ii in range(m):
                matrix[ii][0] = 0
                
        if zero_row is True:
            for jj in range(n):
                matrix[0][jj] = 0
