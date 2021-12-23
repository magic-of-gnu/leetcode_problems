# 79. Word Search

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


# 05 June 2021


class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):

        if not board:
            return False

        nrows = len(board)
        ncols = len(board[0])

        if len(word) > nrows * ncols:
            return False

        def check_combination(board, word, search_inds, ind):
            # print(f'\ncheck_combination')
            # print(f'board: {board}')
            # print(f'word: {word} ind: {ind}')
            # print(f'search_inds: {search_inds}')

            ii, jj = search_inds

            if ii >= 0 and ii < nrows and jj >= 0 and jj < ncols:
                # print(f'inside board')
                if board[ii][jj] == word[ind]:
                    # print(f'on board map')

                    tmp = board[ii][jj]
                    board[ii][jj] = '-'
                    answer = search_two_letters(board, word, (ii, jj), ind=ind)
                    board[ii][jj] = tmp

                    if answer is True:
                        return answer

            return False

        def search_two_letters(board, word, search_inds, ind):
            # print(f'search_two_letters')
            # print(f'ind: {ind}, len(word): {len(word)}')
            # print(f'ii, jj: {search_inds}')
            if ind >= len(word) - 1:
                return True

            ii, jj = search_inds


            # north
            _ii, _jj = ii - 1, jj
            # print(f'north')
            # print(f'board: {board}')
            # print(f'board_map: {board_map}')
            # print(f'word: {word} ind: {ind+1}')
            # print(f'search_inds: {(_ii, _jj)}')
            answer = check_combination(board, word, (_ii, _jj), ind + 1)
            if answer is True:
                return True

            # east
            _ii, _jj = ii, jj + 1
            # print(f'\neast')
            # print(f'board: {board}')
            # print(f'board_map: {board_map}')
            # print(f'word: {word} ind: {ind+1}')
            # print(f'search_inds: {(_ii, _jj)}')
            answer = check_combination(board, word, (_ii, _jj), ind + 1)
            if answer is True:
                return True

            # south
            _ii, _jj = ii + 1, jj
            # print(f'\nsouth')
            # print(f'board: {board}')
            # print(f'board_map: {board_map}')
            # print(f'word: {word} ind: {ind+1}')
            # print(f'search_inds: {(_ii, _jj)}')
            answer = check_combination(board, word, (_ii, _jj), ind + 1)
            if answer is True:
                return True

            # west
            _ii, _jj = ii, jj - 1
            # print(f'\nwest')
            # print(f'board: {board}')
            # print(f'board_map: {board_map}')
            # print(f'word: {word} ind: {ind+1}')
            # print(f'search_inds: {(_ii, _jj)}')
            answer = check_combination(board, word, (_ii, _jj), ind + 1)
            if answer is True:
                return True

            return False


        # construct board with dict
        # print(f'board: {board}')

        for ii in range(nrows):
            for jj in range(ncols):
                ans = check_combination(board, word, (ii, jj), 0)

                if ans is True:
                    return True
                
        return False


if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    answer = False

    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "ABC"
    # answer = True

    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    # word = "EECSEC"
    # answer = True

    # board = [["a","a"]]
    # word = "aaa"


    sol = Solution()
    print(sol.exist(board, word))
