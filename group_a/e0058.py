# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

# A word is a maximal substring consisting of non-space characters only.

# 2021 may 29


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        counter = 0

        s = s.strip()

        if s == '':
            return 0

        for char in reversed(s):
            if char != ' ':
                counter += 1
            else:
                break

        return len(s[-counter:])


if __name__ == "__main__":
    s = " "
    ans = 0

    s = "cat "
    ans = 0

    # s = "the puppy"
    # ans = 5

    sol = Solution()
    print(sol.lengthOfLastWord(s))




