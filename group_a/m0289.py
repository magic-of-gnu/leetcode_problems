# 289. Game of Life

# According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
# 
#     Any live cell with fewer than two live neighbors dies as if caused by under-population.
#     Any live cell with two or three live neighbors lives on to the next generation.
#     Any live cell with more than three live neighbors dies, as if by over-population.
#     Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# 
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for ii in range(m):
            for jj in range(n):
                # print()
                # calculate num live neighbors within the window of 3 by 3
                s = 0
                for ri in range(-1, 2):
                    for rj in range(-1, 2):
                        # if in board and do not add central value
                        if (0 <= ii + ri < m) and (0 <= jj + rj < n) and not (ri == 0 and rj == 0):
                            # print(f'ii: {ii + ri} jj: {jj + rj}')
                            s += board[ii + ri][jj + rj] % 2


                # if not live
                if board[ii][jj] % 2 == 0: 
                    if s == 3:
                        board[ii][jj] = 2
                # if live
                elif board[ii][jj] % 2 == 1:
                    if s == 2 or s == 3:
                        board[ii][jj] = 3
                    else:
                        board[ii][jj] = 1

                # print(f's: {s}')
                # print(f'old: {board[ii][jj] % 2} new: {board[ii][jj] // 2}')
                # print(f'board: {board}')

        for ii in range(m):
            for jj in range(n):
                board[ii][jj] = board[ii][jj] // 2

        print(board)


if __name__ == "__main__":
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Output = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

    board = [[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
    Output = [[1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,0,1],[1,1,1,1]]

    sol = Solution()
    print(sol.gameOfLife(board))
