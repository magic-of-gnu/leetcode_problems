class Solution:
    def alphabetBoardPath2(self, target):
        def get_board_path(board):
            d = {board[row][col]: (row, col) for row in range(len(board)) for col in range(len(board[row]))}
            return d

        def get_position(d, char):
            return d[char]

        def diff2path(diff):
            result = []
            if diff[0] > 0:  # 3
                result.append(diff[0]*"D") # DDD
            elif diff[0] < 0:
                result.append(-diff[0]*"U") 

            if diff[1] > 0: # 0
                result.append(diff[1]*"R")
            elif diff[1] < 0:
                result.append(-diff[1]*"L")

            return result # DDD
        

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        d = get_board_path(board)
        result = []
        current_position = 0, 0
        current_char = "a"
        for char in target:  # l   e    e   t   z   w
            new_position = get_position(d, char) # 4, 2
            if current_char == char:  # t  z
                result.append("!")
                continue

            if char == "z": # 
                new_position = get_position(d, "u") # 4, 0
                diff = [new_position[0] - current_position[0], new_position[1] - current_position[1]] # 1, -4
                current_path = diff2path(diff) # DLLLL
                result.extend(current_path + ["D!"])  # DDR!UURRR!DDD!DLLLLD!
                current_position = get_position(d, "z")  # 5, 0
                current_char = char  # z
                continue

            if current_char == "z":
                result.append("U")  # DDR!UURRR!DDD!DLLLLD!U
                current_position = get_position(d, "u") # 4,  0
                current_char = "u"  # u

            diff = [new_position[0] - current_position[0], new_position[1] - current_position[1]] # 0, 2
            current_path = diff2path(diff)  # RR
            result.extend(current_path + ["!"])  # DDR!UURRR!DDD!DLLLLD!URR!
            current_position = new_position   # 3, 4
            current_char = char               # t

        return "".join(result)


    def alphabetBoardPath(self, target):
        def get_board_path(board):
            d = {board[row][col]: (row, col) for row in range(len(board)) for col in range(len(board[row]))}
            return d

        def get_position(d, char):
            return d[char]
        
        def get_ud(val):
            if val > 0:
                return "D"*val
            elif val < 0:
                return "U"*-val
            else: # val == 0
                return ''
            
        def get_rl(val):
            if val > 0:
                return "R"*val
            elif val < 0:
                return "L"*-val
            else: # val == 0
                return ''

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d = get_board_path(board)

        current_char = "a"
        current_pos = 0,0
        result = []

        for char in target:
            new_pos = get_position(d, char)
            diff_pos = new_pos[0] - current_pos[0], new_pos[1] - current_pos[1]

            if current_char == char:
                result.append("!")
                current_char, current_pos = char, new_pos
                continue

            res_ud = get_ud(diff_pos[0])
            res_rl = get_rl(diff_pos[1])

            if current_char == "z":
                result.append(res_ud)
                result.append(res_rl)
            elif char == 'z':
                result.append(res_rl)
                result.append(res_ud)
            else:
                result.append(res_rl)
                result.append(res_ud)

            result.append("!")
            current_char, current_pos = char, new_pos

        return "".join(result)


if __name__ == "__main__":
    target = "leetzw"
    # target = "leet"
    output = "DDR!UURRR!!DDD!"

    sol = Solution()
    print(sol.alphabetBoardPath(target))
