class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return

        longest_palindrome = s[0]

        n = len(s)

        for window_length in [2,3]:
            for ii in range(n - window_length + 1):
                start = ii
                end = start + window_length - 1

                # print()
                # print(f'ii: {ii}')
                # print(f'start: {start} end: {end}')
                # print(f'window_length: {window_length}')
                # print(f'longest_palindrome: {longest_palindrome}')

                while True:
                    # print(f'start: {start} end: {end}')
                    if not(0 <= start < n and 0 <= end < n):
                        break

                    # print(f'current_str: {s[start:end+1]}')

                    if s[start] != s[end]:
                        break
                    else:
                        # print('here')
                        longest_palindrome = max([longest_palindrome, s[start:end+1]], key=len)
                        start -= 1
                        end += 1

        return longest_palindrome
        
if __name__ == "__main__":
    s = "babadda"

    sol = Solution()
    print(sol.longestPalindrome(s))
