class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_value = str(n)

        # 4553
        # 4449

        for idx, char in enumerate(str_value[:-1]):
            if char > str_value[idx+1]:
                break

        # if idx == len(str_value) - 1:
        #     return n

        print(f'idx: {idx} char: {char}')
        print(f'len(str_value): {len(str_value)}')

        value_left = str(int(char) - 1)
        value_right = '9'
        print(f'value_left: {value_left} value_right: {value_right}')

        if value_left == '0':
            return int('9'*(len(str_value)-1))

        result = 0
        for ii in range(len(str_value)):
            if ii < idx:
                result = 10*result + int(min(value_left, str_value[ii]))
            elif ii == idx:
                if result % 10 < int(str_value[ii-1]):
                    result = 10*result + int(min(value_left, str_value[ii]))
                else:
                    result = 10*result + int(value_right)
            else:
                result = 10*result + int(value_right)

        return result


if __name__ == "__main__":

    n = 1231
    output = 1229

    n = 1022
    n = 1100
    n = 9900
    n = 2200
    n = 111100

    n = 1234
    n = 332

    sol = Solution()
    print(sol.monotoneIncreasingDigits(n))
