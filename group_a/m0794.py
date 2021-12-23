# 794. Valid Tic-Tac-Toe State

# Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

# The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.
# 
# Here are the rules of Tic-Tac-Toe:
# 
#     Players take turns placing characters into empty squares ' '.
#     The first player always places 'X' characters, while the second player always places 'O' characters.
#     'X' and 'O' characters are always placed into empty squares, never filled ones.
#     The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
#     The game also ends if all squares are non-empty.
#     No more moves can be played if the game is over.


class Solution:
    def validTicTacToe(self, board):
        x_count = y_count = 0
        count_x = {f'{l}{x}':0 for x in range(3) for l in 'ij'}
        count_x.update({'d0': 0, 'd1': 0})
        count_y = {f'{l}{x}':0 for x in range(3) for l in 'ij'}
        count_y.update({'d0': 0, 'd1': 0})
        x_won = False

        for ii in range(3):
            for jj in range(3):
                s = board[ii][jj]

                if s == 'X': 
                    count_x[f'i{ii}'] += 1
                    count_x[f'j{jj}'] += 1
                    x_count += 1
                elif s == 'O':
                    count_y[f'i{ii}'] += 1
                    count_y[f'j{jj}'] += 1
                    y_count += 1
                elif s == ' ':
                    continue
                else:
                    return False

            if board[ii][ii] == 'X':
                count_x['d0'] += 1
            
            if board[ii][-ii-1] == 'X':
                count_x['d1'] += 1

            if board[ii][ii] == 'O':
                count_y['d0'] += 1
            
            if board[ii][-ii-1] == 'O':
                count_y['d1'] += 1

        if any([True if x == 3 else False for x in count_x.values()]):
            x_won = True

        if any([True if x == 3 else False for x in count_y.values()]):
            y_won = True

        if x_count - y_count < 0:
            print('qwe')
            return False
        if x_count == y_count and x_won is True:
            print('qwe2')
            return False
        if x_count - y_count > 1:
            print('qwe3')
            return False
        if x_count > y_count and y_won is True:
            print('qwe4')
            return False

        return True

if __name__ == "__main__":
    board = ["O  ","   ","   "]
    Output = False

    board = ["XXX","   ","OOO"]
    Output = False

    board = ["XXX","OOX","OOX"]
    Output = True

    board = ["OXX","XOX","OXO"]
    Output = False

    sol = Solution()
    print(sol.validTicTacToe(board))
