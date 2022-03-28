class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        M, N = m, n

        dp = {(mm,nn):0 for mm in range(m+1) for nn in range(n+1)}

        for s in strs:
            sums = [0, 0]
            for char in s:
                sums[char=='1'] += 1
            # print(f's: {s} sums: {sums}')
            for mm in reversed(range(sums[0],M+1)):
                for nn in reversed(range(sums[1],N+1)):
                    dp[(mm, nn)] = max([1+dp.get((mm-sums[0],nn-sums[1]), 0), dp.get((mm,nn))])


        print(dp)

        return max(dp.values())


if __name__ == "__main__":
    strs = ["10","0001","111001","1","0"]; m = 5; n = 3

    sol = Solution()
    print(sol.findMaxForm(strs, m, n))

