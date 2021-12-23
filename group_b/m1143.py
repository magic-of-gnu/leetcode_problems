# 1143. Longest Common Subsequence

# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        def get_largest_subsequence(text1, text2, memo, ii, jj, count):
            if ii == len(text1) or jj == len(text2):
                memo[(ii, jj)] = 0
                count = max(count, 0)
                return count

            # if the same character, increment both pointers
            if text1[ii] == text2[jj]:
                if memo.get((ii+1, jj+1)) is None:
                    get_largest_subsequence(text1, text2, memo, ii+1, jj+1, count)

                memo[(ii, jj)] = 1 + memo[(ii+1, jj+1)]
                count = max(memo[(ii,jj)], count)
                return count

            # if different characters
            # increment ii, then jj
            else:
                if memo.get((ii+1, jj  )) is None:
                    get_largest_subsequence(text1, text2, memo, ii+1, jj  , count)

                if memo.get((ii  , jj+1)) is None:
                    get_largest_subsequence(text1, text2, memo, ii  , jj+1, count)

                memo[(ii, jj)] = max([memo.get((ii+1, jj)), memo.get((ii, jj+1))])
                count = max(count, memo[(ii,jj)])
                return count


        memo = dict()

        count = get_largest_subsequence(text1, text2, memo, 0, 0, 0)
        return count
