# 1432. Max Difference You Can Get From Changing an Integer

# You are given an integer num. You will apply the following steps exactly two times:
# 
#     Pick a digit x (0 <= x <= 9).
#     Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
#     Replace all the occurrences of x in the decimal representation of num by y.
#     The new integer cannot have any leading zeros, also the new integer cannot be 0.
# 
# Let a and b be the results of applying the operations to num the first and second times, respectively.
# 
# Return the max difference between a and b.


class Solution:
    def maxDiff(self, num: int) -> int:

        a = ''
        to_replace = None
        b = ''
        to_replace_b = None
        b_idx0 = False

        for idx, digit in enumerate(str(num)):
            # a
            if to_replace is None and digit != '9':
                to_replace = digit

            if to_replace is not None and digit == to_replace:
                a += '9'
            else:
                a += digit

            # b
            if to_replace_b is None:
                if idx == 0:
                    if digit != '1':
                        to_replace_b = digit
                        b_idx0 = True
                else:
                    if digit != '0' and digit != '1':
                        to_replace_b = digit

            if to_replace_b is not None and digit == to_replace_b:
                if b_idx0 is True:
                    b += '1'
                else:
                    b += '0'
            else:
                b += digit

        return int(a) - int(b)

if __name__ == "__main__":
    num = 555
    Output = 888 # 999 - 111

    num = 123456112
    num = 200000

    num = 111

    sol = Solution()
    print(sol.maxDiff(num))
