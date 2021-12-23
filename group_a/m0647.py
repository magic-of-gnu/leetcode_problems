class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(s)
        n = count

        for window_length in [2,3]:
            for ii in range(n - window_length + 1):
                start = ii
                end = start + window_length - 1

                while True:
                    if not(0 <= start and end < n):
                        break
                    
                    if s[start] != s[end]:
                        break
                    else:
                        count += 1
                        start -= 1
                        end += 1

        return count


if __name__ == '__main__':
    s = "abbaadda"

    sol = Solution()
    print(sol.countSubstrings(s))
