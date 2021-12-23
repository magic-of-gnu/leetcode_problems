class Solution:

    def coinChange(self, coins, amount: int) -> int:
        
        if amount == 0:
            return 0
        
        # coins amount
        # we will jump from 0 till some coin
        # {0:1} # iterate from the left through the coins
        # {0:1, 1:1, 2:1, 5:1} pop the lowest, iterate through coins -> {1:1, 2:1, 5:1}
        # {1:1, 2:1 or 2, 3:2, 5:1, 6:2} pop the lowest, iterate through coins -> {2:1, 3:2, 5:1, 6:2}
        # {2:1, 3:2 or 2, 4:2, 5:1, 6:1, 7:2} -> {3:2, 4:2, 5:1, 6:2, 7:2}
        # {6:2, 7:2 or 3, 8:3 or 3, 9:3, 10:2, 11:3} -> {7:2, 8:3, 9:3, 10:2, 11:3}
        # {7:2, 8:3 or 3, 9:3 or 3, 10:2, 11:3, 12N} -> {8:3, 9:3, 10:2, 11:3}
        # {8:3, 9:3 or 4, 10:2 or 4, 11:3, Nnoe} -> {9:3, 10:2, 11:3}
        # {9:3, 10:2 or 4, 11:3 or 4, None} -> {10:2, 11:3}
        # {10:2, 11:3} -> {11:3 or 3}
        
        memo = [0] * (amount+1)
        for coin in coins:
            if coin == amount:
                return 1
            if coin < amount:
                memo[coin] = 1

        result = -1
        for val in range(amount):
            if memo[val] == 0:
                continue

            for coin in coins:
                s = val + coin
                if s > amount:
                    continue
                if memo[s] != 0:
                    memo[s] = min(memo[s], memo[val] + 1)
                else:
                    memo[s] = memo[val] + 1

        if memo[amount] == 0:
            return - 1

        return memo[amount]
        
    def coinChange3(self, coins, amount: int) -> int:
        
        if amount == 0:
            return 0
        
        # coins amount
        # we will jump from 0 till some coin
        # {0:1} # iterate from the left through the coins
        # {0:1, 1:1, 2:1, 5:1} pop the lowest, iterate through coins -> {1:1, 2:1, 5:1}
        # {1:1, 2:1 or 2, 3:2, 5:1, 6:2} pop the lowest, iterate through coins -> {2:1, 3:2, 5:1, 6:2}
        # {2:1, 3:2 or 2, 4:2, 5:1, 6:1, 7:2} -> {3:2, 4:2, 5:1, 6:2, 7:2}
        # {6:2, 7:2 or 3, 8:3 or 3, 9:3, 10:2, 11:3} -> {7:2, 8:3, 9:3, 10:2, 11:3}
        # {7:2, 8:3 or 3, 9:3 or 3, 10:2, 11:3, 12N} -> {8:3, 9:3, 10:2, 11:3}
        # {8:3, 9:3 or 4, 10:2 or 4, 11:3, Nnoe} -> {9:3, 10:2, 11:3}
        # {9:3, 10:2 or 4, 11:3 or 4, None} -> {10:2, 11:3}
        # {10:2, 11:3} -> {11:3 or 3}
        
        memo = {coin: 1 for coin in [0] + coins}
        lowest = min(coins)
        result = -1
        
        while memo and lowest < amount:

            lowest = min(memo)
            print()
            print(f'lowest: {lowest}')
            print(f'memo: {memo}')

            for coin in coins:
                print(f'coin: {coin}')
                s = lowest + coin
                print(f's: {s}')
                
                if s > amount:
                    continue
                    
                memo[s] = min(memo.get(s, float('inf')), memo[lowest] + 1)
                print(f'new memo: {memo}')
                
            result = memo[lowest]
                
            if memo:
                memo.pop(lowest)
                
            
        print(f'memo: {memo}')
        print(f'result: {result}')
        print(f'lowest: {lowest}')
            
        if lowest != amount:
            return -1
        
        return result


if __name__ == '__main__':

     nums = [2,5,10,1]
     amount = 27

     nums = [474, 83, 404, 3]
     amount = 264
     expected = 8

     # nums = [2]
     # amount = 3

     sol = Solution()
     print(sol.coinChange(nums, amount))

