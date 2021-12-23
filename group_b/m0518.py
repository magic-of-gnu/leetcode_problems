# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/

from collections import deque

class Solution:
    # def change(self, amount: int, coins: List[int]) -> int:
    def change2(self, amount, coins):

        def get_gcd(a, b):
            if b > a:
                a, b = b, a
            if b == 0:
                return a
            return get_gcd(b, a%b)

        def get_lcm(a, b):
            nom = a * b
            den = get_gcd(a,b)
            return int(nom/den)

        def _get_lcm(arr):
            lcm = arr[0]
            for x in arr[1:]:
                lcm = get_lcm(lcm, x)
            return lcm

        lcm = _get_lcm(coins)
        count_lcm = amount // lcm
        rems = {0: dict()}
        combinations = set()

        for val in range(1, lcm+1):
            combs = set()
            for coin in coins:
                if rems.get(val-coin, None) is not None:
                    _combs = {tuple(sorted(list(key) + [coin])): 1  for key in rems[val-coin]}
                    if not _combs:
                        _combs = {tuple([coin]): 1}
                    combs = combs.union(_combs)
            rems[val] = combs
            combinations = combinations.union(combs)
        print(f'combinations.len: {len(combinations)}')

        if rems.get(amount%lcm, None) is None:
            return 0

        return count_lcm * len(combinations) + len(rems[amount%lcm])

    def change1(self, amount, coins):
        if amount == 0:
            return 0

        if len(coins) == 1:
            return int(amount % coins[0] == 0)

        def dfs(coins, ii, current_sum, amount, count):
            if ii > n - 1:
                return

            if current_sum + coins[ii] == amount:
                count[0] += 1
                print(f'increasing count, new count: {count}')
                return
            elif current_sum + coins[ii] > amount:
                return
            else:
                if ii == n-1:
                    return dfs(coins, n-1, current_sum + coins[ii], amount, count)

                for jj, x in enumerate(coins[ii:], start=ii):
                    if current_sum + coins[ii] + coins[jj] > amount:
                        break
                    dfs(coins, jj, current_sum + coins[ii], amount, count)


        count = [0]
        n = len(coins)

        coins.sort()
        for ii in range(n):
            dfs(coins, ii, 0, amount, count)
        return count[0]


    def change(self, amount, coins):

        if amount == 0:
            return 1

        def check_conjugate(coin, amount, results, count):
            s = coin

            while True:
                if s > amount:
                    break
                elif s == amount:
                    count[0] += 1

                if results[amount-s] > 0:
                    count[0] += results[amount-s]

                s += coin

        def add_coin_combinations(coin, amount, results):
            values = [0] + [x for x in results if results.get(x) > 0]
            s = coin

            while True:
                if s >= amount:
                    break

                for v in values:
                    if v+s >= amount:
                        break
                    results[v+s] += 1

                s += coin


        coins.sort()

        n = len(coins)
        results = {x: 0 for x in range(amount)}
        count = [0]
        
        # idea is to firstly check for conjugate in results
        # then add current coin and all of its possible sums to results

        counter = 0

        for ii in range(n-1, -1, -1):
            check_conjugate(coins[ii], amount, results, count)
            add_coin_combinations(coins[ii], amount, results)
            print(f'coin: {coins[ii]}')
            print(results)
            print(count)

            counter += 1

            # if counter > 2:
            #     break






if __name__ == "__main__":
    amount = 5
    coins = [1,2,5]
    Output = 4

    amount = 100
    coins = [2,3,4,6,8]
    Output = 5860

    # amount = 500
    # coins = [3,5,7,8,9,10,11]
    # Output = 35502874

    sol = Solution()
    print(sol.change(amount, coins))
