from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = defaultdict(int)
        max_window = 1

        for right in range(len(s)):
            d[s[right]] += 1
            if all(val == 1 for val in d.values()):
                max_window = max(max_window, right-left+1)
                print(f'left: {left} right: {right} max_window: {max_window}')
            else:
                # d[s[right]] += 1
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    d.pop(s[left])

                left += 1

        return max_window



if __name__ == "__main__":
        #012345
    s = "pwwkew"
    s = "bbbbb"
        #01234567
    # s = "abcabcbb"

    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))

