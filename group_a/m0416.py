class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)         # 12

        next_sums, next_diffs = {0:1}, {total_sum:1}

        for num in nums:                            # 11
            sums, diffs = next_sums, next_diffs

            # next_sums, next_diffs = [], []

            for s, d in zip(list(sums.keys()), list(diffs.keys())):           # 0  22;  1  10
                ns, nd = s + num, d - num           # 11 11
                if ns == nd:
                    return True
                next_sums[ns] = 1              # 5 6
                next_diffs[nd] = 1


        return False

