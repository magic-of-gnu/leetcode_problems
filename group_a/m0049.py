from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        if len(strs) == 0:
            return [[""]]

        if len(strs) == 1:
            return [strs]

        def count_letters(word, d):
            _d = {x: 0 for x in d.keys()}

            if not word:
                return _d

            for char in word:
                _d[char] += 1

            return _d

        # results = defaultdict(set)
        results = defaultdict(list)
        d = {x: 0 for x in "qwertyuiopasdfghjklzxcvbnm"}

        for word in strs:
            counter = count_letters(word, d)
            results[str(counter)].append(word)

        if len(results.values()) == 0:
            return [[""]]

        return [list(item) for item in results.values()]


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs =  ["",""]

    sol = Solution()
    print(sol.groupAnagrams(strs))
