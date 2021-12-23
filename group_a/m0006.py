# 6. ZigZag Conversion

# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string s, int numRows);
# 


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        do the counter if rem < numRows: row_counter +=1 else row_counter-=1
        append list of lists or strings [[str]]
        row0    rem0
        row1    rem1          rem7
        row2    rem2      rem6
        row3    rem3  rem5
        row4    rem4
        '''

        if not s:
            return s

        if numRows == 1:
            return s

        n = 2 * numRows - 2
        row_counter = 0

        answer = [list() for x in range(numRows)]

        for idx, char in enumerate(s):
            # print()
            rem = idx % n

            # print(f'idx: {idx}, char: {char} rem: {rem}')
            # print(f'row_counter: {row_counter}')

            answer[row_counter].append(char)

            if rem < numRows-1:
                row_counter += 1
            else:
                row_counter -= 1

        converted = ''
        for row in answer:
            converted += ''.join(row)

        return converted



if __name__ == "__main__":
    s = "PAYPALISHIRING"; numRows = 3
    ans = "PAHNAPLSIIGYIR"

    s = "a"
    numRows = 1


    sol = Solution()
    print(sol.convert(s, numRows))

