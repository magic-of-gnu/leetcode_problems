class Solution:
    def mincostTickets2(self, days, costs):
        dp = [0] * (max(days) + 1)
        jj = 0

        for ii in range(1,len(dp)): # 2
            if ii == days[jj]:      # 2
                jj += 1             # 2
            else:
                dp[ii] = dp[ii-1]
                continue

            dp[ii] = min([
                dp[ii-1]+costs[0],           # 2
                dp[max(0,ii-7)]+costs[1],    # 7
                dp[max(0,ii-30)]+costs[2],   # 15
            ])

        return dp[-1]


if __name__ == "__main__":
    days = [1,2,3,4,5,6,7,8,9,10,30,31]; costs = [2,7,15]

    sol = Solution()
    print(sol.mincostTickets(days, costs))
