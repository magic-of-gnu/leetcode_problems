# 1048. Longest String Chain

# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.
# 
#     For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
# 
# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.
# 
# Return the length of the longest possible word chain with words chosen from the given list of words.

from collections import defaultdict


class Solution:
    # def longestStrChain(self, words: List[str]) -> int:
    def longestStrChain(self, words):

        def is_predecessor(word_a, word_b):
            count = 0

            na = len(word_a)
            nb = len(word_b)

            ind_a, ind_b = 0, 0

            while count < 2 and (ind_a < na and ind_b < nb):
                if word_a[ind_a] == word_b[ind_b]:
                    ind_a += 1
                else:
                    count += 1

                ind_b += 1

            if count == 2:
                return False
            return True

        counter = defaultdict(list)
        max_count = 0
        results = dict()
        min_l = None
        max_l = 0

        for x in words:
            min_l = len(x) if min_l is None else min(len(x), min_l)
            max_l = max(len(x), max_l)
            counter[len(x)].append(x)

        for l in range(min_l, max_l+1):
            words_l = counter.get(l)
            for word_a in words_l:
                for word_b in counter.get(l+1, []):
                    # print()
                    # print(f'word_a: {word_a} word_b: {word_b}')
                    if is_predecessor(word_a, word_b):
                        count = max(results.get(word_a, 1) + 1, results.get(word_b, 0))
                        max_count = max(count, max_count)
                        results[word_b] = count
                        # print(f'count: {count} max_count: {max_count}')
                        # print(results)


        if max_count == 0:
            return 1
        return max_count



if __name__ == "__main__":
    words = ["a","b","ba","bca","bda","bdca"]
    Output = 4

    words = ['a', 'b', 'c', 'ab', 'ac', 'ad', 'df', 'abc', 'qwe', 'qzsdeq', 'dfe', 'abcd', 'dfeg', 'qqqq', 'zqwe', 'abcd', 'dfegh', 'dfeghi']

    words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

    words = ["a","ab","ac","bd","abc","abd","abdd"]

    sol = Solution()
    print(sol.longestStrChain(words))
        
