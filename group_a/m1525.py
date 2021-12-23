# 1525. Number of Good Ways to Split a String

# You are given a string s, a split is called good if you can split s into 2 non-empty strings p and q where its concatenation is equal to s and the number of distinct letters in p and q are the same.

# Return the number of good splits you can make in s.

# 2021 May 31


class Solution:
    def numSplits(self, s: str) -> int:
        '''
        Create a list of ints, where each int means the amount of distinct letters appeared up to current lookup position

        Find the middle amount of distinct letterts, then count possible ways to split the string
        '''

        counter_forward = [0 for _ in range(len(s))]
        counter_backward = [0 for _ in range(len(s))]

        c_f = dict()
        c_b = dict()

        d_forward = dict()
        d_backward = dict()

        cf = 0
        cb = 0

        for ii in range(len(s)):
            jj = -(ii + 1)
            char_f = s[ii]
            char_b = s[jj]

            # new letter
            if d_forward.get(char_f, None) is None:
                d_forward[char_f] = 1
                cf += 1

            counter_forward[ii] = cf

            # new letter
            if d_backward.get(char_b, None) is None:
                d_backward[char_b] = 1
                cb += 1

            counter_backward[jj] = cb

        counter = 0

        for ii in range(len(s)-1):
            jj = ii + 1
            cf = counter_forward[ii]
            cb = counter_backward[jj]

            if cf == cb:
                counter += 1

        return counter


if __name__ == "__main__":
    s = "aacaba"
    num = 2

    s = "ababbbbbbb"
    num = 1

    sol = Solution()
    print(sol.numSplits(s))
