# 974. Subarray Sums Divisible by K

# Given an array nums of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by k.

class Solution:
    # def subarraysDivByK(self, nums: List[int], k: int) -> int:
    def subarraysDivByK(self, nums, k):
        if not nums:
            return 0
        count = 0
        sums = dict()
        n = len(nums)

        l = 1

        while l <= n:
            for ii in range(0, n + 1 - l ):
                # print()
                # print(f'ii: {ii} l: {l}')
                # print(f'count: {count}')
                _nums = nums[ii:ii+l]
                first = _nums[0]
                rest = _nums[1:]
                _s = sums.get(tuple(rest), 0)

                _sum = first + _s
                sums[tuple(_nums)] = _sum
                if _sum % k == 0:
                    count += 1

                # print(f'_nums: {_nums}')
                # print(f'_s: {_s}')
                # print(f'_sum: {_sum}')
                # print(sums)

            l += 1

        return count


if __name__ == "__main__":
    nums = [4,5,0,-2,-3,1]; k = 5
    Output = 7

    sol = Solution()
    print(sol.subarraysDivByK(nums, k))

