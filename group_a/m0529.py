# 529. Minesweeper
# https://leetcode.com/problems/minesweeper/

from collections import deque

class Solution:
    # def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    def updateBoard(self, board, click):

        n, m = len(board), len(board[0])
        q = dict()
        q[tuple(click)] = 1

        while q:
            # print(f'queue: {q}')
            # keys = list(q.keys())
            # r, c = keys[0]
            # q.pop(keys[0])
            (r, c), _ = q.popitem()
            mines_count = 0

            if board[r][c] == 'M':
                board[r][c] = 'X'
            elif board[r][c] == 'B':
                continue
            elif board[r][c] == 'E':
                to_append = dict()

                if r-1 >= 0 and c-1 >= 0:
                    if  board[r-1][c-1] == 'M':
                        # print('here0')
                        mines_count += 1
                    elif board[r-1][c-1] == 'E':
                        to_append[(r-1,c-1)] = 1
                        # q[(r-1,c-1)] = 1

                if r-1 >= 0:
                    if board[r-1][c] == 'M':
                        # print('here1')
                        mines_count += 1
                    elif board[r-1][c] == 'E':
                        to_append[(r-1,c)] = 1
                        # q[(r-1,c)] = 1

                if r-1 >= 0 and c+1 < m:
                    if board[r-1][c+1] == 'M':
                        # print('here2')
                        mines_count += 1
                    elif board[r-1][c+1] == 'E':
                        to_append[(r-1,c+1)] = 1
                        # q[(r-1,c+1)] = 1

                if c-1 >= 0:
                    if board[r][c-1] == 'M':
                        # print('here3')
                        mines_count += 1
                    elif board[r][c-1] == 'E':
                        to_append[(r,c-1)] = 1
                        # q[(r,c-1)] = 1
                if c+1 < m:
                    if board[r][c+1] == 'M':
                        # print('here4')
                        mines_count += 1
                    elif board[r][c+1] == 'E':
                        to_append[(r,c+1)] = 1
                        # q[(r,c+1)] = 1

                if r+1 < n and c-1 >= 0:
                    if board[r+1][c-1] == 'M':
                        # print('here5')
                        mines_count += 1
                    elif board[r+1][c-1] == 'E':
                        to_append[(r+1,c-1)] = 1
                        # q[(r+1,c-1)] = 1
                if r+1 < n:
                    if board[r+1][c] == 'M':
                        # print('here6')
                        mines_count += 1
                    elif board[r+1][c] == 'E':
                        to_append[(r+1,c)] = 1
                        # q[(r+1,c)] = 1

                if r+1 < n and c+1<m:
                    if board[r+1][c+1] == 'M':
                        # print('here7')
                        mines_count += 1
                    elif board[r+1][c+1] == 'E':
                        to_append[(r+1,c+1)] = 1
                        # q[(r+1,c+1)] = 1

                if mines_count != 0:
                    board[r][c] = str(mines_count)
                else:
                    board[r][c] = 'B'
                    q.update(to_append)

        
        return board



if __name__ == "__main__":
    board = [
            ["E","E","E","E","E"],
            ["E","E","M","E","E"],
            ["E","E","E","E","E"],
            ["E","E","E","E","E"]
    ]
    click = [3,0]

    board = [["E","M","M","E","E","E","E","E"],
             ["E","E","M","E","E","E","E","E"],
             ["E","E","E","E","E","E","E","E"],
             ["E","M","E","E","E","E","E","E"],
             ["E","E","E","E","E","E","E","E"],
             ["E","E","M","E","E","E","E","E"],
             ["E","E","E","E","E","E","E","E"],
             ["E","E","E","E","E","E","E","E"]]
    click = [5,5]


    # ans = \
#0  [["E","M","M","2","B","B","B","B"],
#1   ["E","E","M","2","B","B","B","B"],
#2   ["E","E","2","1","B","B","B","B"],
#3   ["E","M","1","B","B","B","B","B"],
#4   ["E","E","2","1","b","b","B","B"],
#5   ["E","1","M","1","B","b","B","B"],
#6   ["B","1","1","1","B","B","B","B"],
#7   ["B","B","B","B","B","B","B","B"]]
#      0   1   2   3   4   5   6   7  

    # exp = \
#0  [["E","M","M","2","B","B","B","B"],
#1   ["E","E","M","2","B","B","B","B"],
#2   ["E","E","2","1","B","B","B","B"],
#3   ["E","M","1","B","B","B","B","B"],
#4   ["1","2","2","1","B","B","B","B"],
#5   ["B","1","M","1","B","B","B","B"],
#6   ["B","1","1","1","B","B","B","B"],
#7   ["B","B","B","B","B","B","B","B"]]
#      0   1   2   3   4   5   6   7  
   


    sol = Solution()
    print(sol.updateBoard(board, click))
