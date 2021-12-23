# 139. Word Break
# https://leetcode.com/problems/word-break/

from collections import defaultdict

class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    def wordBreak(self, s, wordDict):

        def dfs(inds, val, n):
            if val == n:
                return True

            return any([dfs(inds, val + v + 1, n) for v in inds.get(val, [])])
        
        inds = defaultdict(set)

        iword = 0
        iiw, iis = 0, 0

        nwords = len(wordDict)
        ns = len(s)
        word = wordDict[0]
        d = [0] * ns

        while True:
            # print()

            if iis == ns and iword == nwords - 1:
                # print(f'iis: {iis} iiw: {iiw} word: {word}')
                # print(f'break')
                break

            if iis == ns:
                # print(f'iis: {iis} iiw: {iiw} word: {word}')
                # print(f'reduce')
                iword += 1
                word = wordDict[iword]
                iis = 0
                iiw = 0

            # print(f'iis: {iis} iiw: {iiw} word: {word}')
            # print(f'ls: {s[iis]} lw: {word[iiw]}')

            if s[iis] == word[iiw]:
                

                if iiw == len(word) - 1:
                    inds[iis - iiw].add(iiw)
                    # print(f'iis: {iis} iiw: {iiw}')
                    # print(iis - iiw, iis - iiw - 1)
                    if d[iis] % 2 != 0 or d[iis] == 0:
                        d[iis] += 2
                    if d[iis-iiw] % 2 != 1 or d[iis-iiw] == 0:
                        d[iis-iiw] += 1
                    iis = iis - iiw

                iis += 1

                iiw = (iiw + 1) % len(word)

            else: # s[iis] != word[iiw]
                if iiw != 0:
                    iiw = 0
                else:
                    iis += 1

        # print(inds)
        # print(d)

        reg = 1
        c = [False] * ns

        for ii in range(len(d)):
            if d[ii] == 0:
                continue

            if reg == 1:
                if d[ii] % 2 == 1:
                    reg = 2
            elif reg == 2:
                if ii == ns - 1:
                    if d[ii] % 2 == 0:
                        reg = 1
                        c[ii] = True
                elif d[ii] % 2 == 0 and d[ii+1] % 2 == 1:
                    reg = 1
                    c[ii] = True

        return c[-1]

        # return dfs(inds, 0, len(s))

    def wordBreak3(self, s, words):
       d = [False] * len(s)    
       for i in range(len(s)):
          for w in words:
             if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                 print(d)
                 d[i] = True
       return d[-1]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    Output = True

    s = "applepenapple"
    wordDict = ["pen", "apple"]
    Output = True

    s = "appleappapplea"
    wordDict = ["app", "apple", "applea"]
    Output = True

    # s = "aaaaaaa"
    # wordDict = ["aaaa","aaa"]

    # s = "appleappapple"
    # wordDict = ["app", "apple"]
    # Output = True

    # s = "appleappapple"
    # wordDict = ["app", "appleq"]
    # Output = False

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

    sol = Solution()
    print(sol.wordBreak(s, wordDict))
