# 945. Minimum Increment to Make Array Unique

# Given an array of integers nums, a move consists of choosing any nums[i], and incrementing it by 1.

# Return the least number of moves to make every value in nums unique.

from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, nums):

        if len(nums) == 0:
            return 0

        num_moves = 0

        # construct the counter
        counter = defaultdict(int)
        min_value = 40000 + 1
        max_value = -1

        for x in nums:
            counter[x] += 1
            max_value = max(max_value, x)
            min_value = min(min_value, x)

        num_non_uniques = 0
        value_non_uniques = 0
        next_values = 0

        # two counters
        counter_values = min_value
        counter_keys = min_value
        while True:
            if counter_keys == max_value + 1 and num_non_uniques == 0:
                break

            # find value from counter to be increased
            if num_non_uniques == 0:
                if counter.get(counter_keys, None) is not None:
                    num_non_uniques = counter.get(counter_keys) - 1
                    value_non_uniques += num_non_uniques * counter_keys
                else:
                    num_non_uniques = 0

                counter_keys += 1

            counter_values = max(counter_keys, counter_values)

            if num_non_uniques != 0:
                while True:
                    if counter.get(counter_values, 0) == 0:
                        next_values += counter_values
                        num_non_uniques -= 1

                        counter_values += 1
                        break
                    
                    counter_values += 1

        return next_values - value_non_uniques



if __name__ == "__main__":
    nums = [1,2,2]
    Output = 1

    # nums = [1, 1, 2, 3, 4, 5, 6, 6, 6]

    # nums = [0,2,2]

    # nums = [0, 0]

    sol = Solution()
    print(sol.minIncrementForUnique(nums))
