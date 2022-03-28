
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        if target < n:
            return 0

        prev = {x:1 for x in range(1,k+1)}
        prev.update({x:0 for x in range(k+1, target+1)})
        
        for dice in range(2, n+1):
            curr = {x:0 for x in range(dice, target+1)}
            s = 0

            for ii in range(dice, target+1):
                s += (prev[ii-1] - prev.get(ii-k-1,0))
                curr[ii] = s
        
            prev = curr

        return curr[target] % (10**9+7)


if __name__ == "__main__":
    n, k, target = 3, 6, 12
    n, k, target = 30, 30, 500

    n, k, target = 20, 19, 233

    sol = Solution()
    print(sol.numRollsToTarget(n, k, target))
