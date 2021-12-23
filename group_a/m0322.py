# 322. Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# 
# You may assume that you have an infinite number of each kind of coin.

# https://leetcode.com/problems/coin-change/

class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    def coinChange(self, coins, amount):

        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        # if len(coins) == 1:
        #     if amount % coins[0] == 0:
        #         return amount // coins[0]
        #     return -1

        def get_gcd(a, b):
            if b > a:
                a, b = b, a
            if b == 0:
                return a

            return get_gcd(b, a%b)

        def get_lcm(a, b):
            mul = a * b
            d = get_gcd(a,b)
            return int(mul/d)

        lcm = coins[0]
        for x in coins[1:]:
            lcm = get_lcm(lcm, x)

        max_coin = max(coins)

        coins_per_lcm = lcm // max_coin
        print(f'lcm: {lcm}')
        print(f'coins_per_lcm: {coins_per_lcm}')

        memo = {0:0}

        for x in range(1,amount%lcm+1):
            coin_counts = [memo.get((x-coin)%max_coin) for coin in coins if memo.get((x-coin)%max_coin) is not None]

            if coin_counts:
                memo[x%max_coin] = min(coin_counts) + 1

        print(f'memo: {memo}')
        print(f'amount%max_coin: {amount%max_coin}')
        if memo.get(amount%max_coin) is not None:
            count = (amount // lcm) * coins_per_lcm 
            print(f'count: {count}')
            if count * max_coin != amount:
                count += memo[amount%max_coin]
            return count

        return -1


if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    Output = 3

    coins = [1,2,3,5,10]
    amount = 1551
    amount = 1551

    # coins = [186,419,83,408]
    # amount = 6249

    coins = [10,5,7,3]
    amount = 4
    Output = -1

    coins = [1]
    amount = 1
    Output = 1

    # coins = [2]
    # amount = 2
    # Output = 1

    sol = Solution()
    print(sol.coinChange(coins, amount))
