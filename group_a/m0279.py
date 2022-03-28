class Solution:
    def numSquares(self, n: int) -> int:
        seen_squares = []
        jj = 1

        memo = [0] * (n + 1)

        for ii in range(1, n+1):
            if ii == jj**2:
                seen_squares.append(jj**2)
                memo[ii] = 1
                jj += 1
                continue

            memo[ii] = min([memo[sq] + memo[ii-sq] for sq in seen_squares])

        return memo[-1]


if __name__ == "__main__":
    n = 12

    sol = Solution()
    print(sol.numSquares(n))
