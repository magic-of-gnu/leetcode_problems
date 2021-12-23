class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter_s, counter_t = dict(), dict()
        for val in s:
            if val not in counter_s:
                counter_s[val] = 1
            else:
                counter_s[val] += 1

        for val in t:
            if val not in counter_t:
                counter_t[val] = 1
            else:
                counter_t[val] += 1

        for k, v in counter_t.items():
            if v != counter_s.get(k,0):
                return False

        return True

if __name__ == "__main__":
        s = "anagram"
        t = "nagaram"

        sol = Solution()
        print(sol.isAnagram(s, t))
