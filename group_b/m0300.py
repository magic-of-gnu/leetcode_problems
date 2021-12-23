# 300. Longest Increasing Subsequence

# https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS2(self, nums):

        if not nums:
            return 0

        def dfs(nums, ii, memo):
            # print()
            # print(f'before ii: {ii} memo: {memo}')
            for jj in range(ii+1, n):
                if nums[ii] < nums[jj]:
                    # print(f'ii: {ii} jj: {jj} memo: {memo}')

                    if memo.get(jj) is None:
                        dfs(nums, jj, memo)
                    memo[ii] = max(memo.get(ii, 0), memo[jj] + 1)

            if memo.get(ii) is None:
                memo[ii] = 0
            # print(f'after ii: {ii} memo: {memo}')

        n = len(nums)
        memo = {n-1:0}

        for ii in range(n):
            dfs(nums, ii, memo)
        # print(memo)

        return max(memo.values()) + 1

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            print()
            print(f'x: {x} size: {size} tails: {tails}')
            i, j = 0, size
            print(f'i: {i} j: {j}')
            while i != j:
                m = (i + j) // 2
                print(f'i: {i} j: {j} m: {m}')
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m

            print(f'finished i: {i} j: {j}')
            tails[i] = x
            size = max(i + 1, size)

        return size



if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Output = 4

    nums = [1,2,3,4,5,6]
    Output = 6

    nums = [10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 21]
    nums = [10, 11, 12, 13, 14, 1, 2, 9, 20, 21]

    # nums = [7,6,5,4,3,2,1]
    # Output = 1

    # nums = []
    # Output = 0

    sol = Solution()
    print(sol.lengthOfLIS(nums))

