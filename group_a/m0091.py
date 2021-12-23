# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

from pprint import pprint as pp

class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "0":
            return 0

        memo = {x: 0 for x in range(-1, len(s))}
        memo[-1] = 1

        prev = 4

        for ind, v in enumerate(reversed(s)):
            if v == "0":
                if prev == 0:
                    return 0
                prev = 0
                memo[ind] = memo.get(ind-1, 0)
            elif prev == 0:
                if v > "2":
                    return 0
                prev = 1
                memo[ind] = memo.get(ind-1, 0)
            elif prev == 1:
                prev = 4
                memo[ind] = memo.get(ind-1, 0)
            elif v > "6":
                prev = 2
                memo[ind] = memo.get(ind-1, 0)
            elif v > "2":
                prev = 3
                memo[ind] = memo.get(ind-1, 0)
            elif v > "0" and v < "3":
                if v == "2" and prev == 2:
                    memo[ind] = memo.get(ind-1, 0)
                else:
                    memo[ind] = memo.get(ind-1, 0) + memo.get(ind-2, 0)
                prev = 4

            if v > "6":
                prev = 2
            elif v > "2":
                prev = 3

        if v == "0":
            return 0

        pp(memo)

        return memo[len(s)-1]


if __name__ == "__main__":
    s = "12"
    Output = 2

    # s = "622112016"
    # Output = 10

    # s = "22222222222101010222102022106610"
    # Output = 864

    # s = "01029"
    # Output = 0

    # s = "1029"
    # Output = 1

    s = "111029"
    Output = 2

    s = "10029"
    Output = 0

    sol = Solution()
    print(sol.numDecodings(s))
