# 357. Count Numbers with Unique Digits

# Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        if n == 1:
            return 10

        count = 9
        total = 10
        for x in range(1, n):
            count *= (10 - x)
            total += count

        return total


if __name__ == "__main__":
    n = 2
    Output = 91

    n = 3
    Output = 739

    n = 4
    Output = 5275

    sol = Solution()
    print(sol.countNumbersWithUniqueDigits(n))
