from collections import Counter

class Solution:
    def hIndex(self, citations):

        citations.sort()
        cpos, cneg = dict(), dict()
        n = len(citations)
        val = 0

        cpos = {0: n}
        cneg = {0: 0}
        counter = 0
        citations_counter = Counter(citations)

        for ind, cit in enumerate(citations):
            if cit != 0:
                cpos[cit] = n - counter
                cneg[cit] = counter
            counter += citations_counter[cit]

        for key, val in reversed(cpos.items()):
            if key >= val and cneg[key] == n - key:
                return key



if __name__ == "__main__":
    citations = [3,0,6,1,5,100]
    output = 3

    sol = Solution()
    print(sol.hIndex(citations))
        
