class Solution:
    def isPalindrome2(self, s: str) -> bool:
        allowed_chars = set("qwertyuiopasdfghjklzxcvbnm1234567890")

        s = ''.join([char.lower() for char in s if char.lower() in allowed_chars])

        ii, jj = 0, len(s) - 1

        while ii < jj:
            if s[ii] != s[jj]:
                return False

            ii += 1
            jj -= 1

        return True

    def isPalindrome(self, s: str) -> bool:
        ii, jj = 0, len(s) - 1

        while ii < jj:

            if not s[ii].isalnum():
                ii += 1

            if not s[jj].isalnum():
                jj -= 1

            if s[ii].isalnum() and s[jj].isalnum():
                if s[ii].lower() != s[jj].lower():
                    return False

                ii += 1
                jj -= 1

        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"

    sol = Solution()
    print(sol.isPalindrome(s))
