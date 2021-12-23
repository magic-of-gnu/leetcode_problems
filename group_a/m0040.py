# 40. Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# 
# Each number in candidates may only be used once in the combination.
# 
# Note: The solution set must not contain duplicate combinations.

from copy import deepcopy

class Solution:
    def combinationSum2(self, candidates, target):

        def get_sum(candidates, target, current_combination, current_sum, prev_key):

            can = deepcopy(candidates)
            keys = [x for x in can.keys() if x >= prev_key]

            for key in keys:
                # print()
                value = can[key]
                can[key] -= 1
                # print(f'candidates: {can}')
                # print(f'target: {target} key: {key}')
                # print(f'current_combitation: {current_combination}')
                # print(f'current_sum: {current_sum}')
                if value > 0:
                    if current_sum + key > target:
                        # print(f'\nreturning:')
                        # print(f'candidates: {candidates}')
                        # print(f'target: {target} key: {key}')
                        # print(f'current_combitation: {current_combination}')
                        # print(f'current_sum: {current_sum}')
                        return 

                    if current_sum + key == target:
                        # print(f'\nappending:')
                        # print(f'candidates: {candidates}')
                        # print(f'target: {target} key: {key}')
                        # print(f'current_combitation: {current_combination}')
                        # print(f'current_sum: {current_sum}')
                        # results.add(tuple(current_combination + [key]))
                        results.add(tuple(current_combination + [key]))

                    if current_sum + key < target:
                        get_sum(can, target, current_combination + [key], current_sum + key, key)

                can[key] += 1

            return

            


        cans = {x:0 for x in range(1, 50)}

        for x in candidates:
            cans[x] += 1

        cans = {key: value for key, value in cans.items() if value}

        results = set()
        current_sum = 0

        get_sum(cans, target, [], current_sum, -1)
        return [list(x) for x in results]



if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    output = [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]

    candidates = [2,5,2,1,2]
    target = 5

    sol = Solution()
    a = sol.combinationSum2(candidates, target)
