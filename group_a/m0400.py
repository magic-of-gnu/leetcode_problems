# 400. Nth Digit

# Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].


class Solution:
    def findNthDigit(self, n: int) -> int:
        k = n
        x = 1

        while True:
            num_digits = x * 9 * 10**(x-1)
            if k - num_digits < 0:
                break
            k -= num_digits
            x += 1

        val = 10**(x - 1) + k // x + int(k%x>0) - 1
        return str(val)[k%x - 1]


if __name__ == "__main__":
    n = 11
    Output = 0

    n = 187


    sol = Solution()
    print(sol.findNthDigit(n))
        
