# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        m, n = min(m,n), max(m,n)

        memo = [1] * (m-2)

        for r in range(2, n+1):
            print(memo)
            for c in range(2,m):
                r += memo[c-2]
                memo[c-2] = r

        return r

if __name__ == "__main__":
    m, n = 3, 7
    Output = 28

    m, n = 10, 15
    Output = 817190

    sol = Solution()
    print(sol.uniquePaths(m, n))

