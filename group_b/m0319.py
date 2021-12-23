# 319. Bulb Switcher

# There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.
# 
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.
# 
# Return the number of bulbs that are on after n rounds.

class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = [1 for _ in range(n)]

        for ii in range(2, n+1):
            for bulb in range(ii,n+1, ii):
                bulbs[bulb-1] ^= 1

        return sum(bulbs)

        pass


if __name__ == "__main__":
    n = 3
    Output = 1

    n = 15
    Output = 3
    
    sol = Solution()
    print(sol.bulbSwitch(n))
