class Solution:
    def knightDialer2(self, n: int) -> int:

        if n == 1:
            return 10

        def dfs(num, curr_n, memo, moves_map, results):

            if curr_n == 0:
                results[0] += 1
                memo[(num,curr_n)] = 1
                return 1

            if (num,curr_n) in memo:
                results[0] += memo[(num,curr_n)]
                return memo[(num,curr_n)]

            count = 0

            for next_num in moves_map[num]:

                count += dfs(next_num, curr_n-1, memo, moves_map, results)

            memo[(num,curr_n)] = count

            return count


        results = [0]
        memo = dict()
        moves_map = {
            "1": "68",
            "2": "79",
            "3": "48",
            "4": "390",
            "6": "170",
            "7": "26",
            "8": "13",
            "9": "24",
            "0": "46"
        }
        for num in "012346789":
            dfs(num, n-1, memo, moves_map, results)

        return results[0] % (10**9+7)


    def knightDialer(self, n):

        if n == 1:
            return 10

        result = 0
        moves_map = {
            "1": "68",
            "2": "79",
            "3": "48",
            "4": "390",
            "6": "170",
            "7": "26",
            "8": "13",
            "9": "24",
            "0": "46"
        }
        memo = dict()
        nums_map = {"0": 1, "1":2, "2":1, "4":2, "7":2, "8":1}
        for num, coef in nums_map.items():
            dp = defaultdict(int)
            dp[num] = 1
            for moves_count in range(1, n):
                next_dp = defaultdict(int)
                for next_num, v in dp.items():
                    for next_num2 in moves_map[next_num]:
                        next_dp[next_num2] += v

                dp = next_dp

            result += (sum(dp.values()) * coef)

        return result % (10**9+7)
