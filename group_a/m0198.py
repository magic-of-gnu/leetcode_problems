class Solution:
    # def rob(self, nums: List[int]) -> int:
    def rob(self, nums):
        vold, s1, s2 = 0, 0, 0

        for ind in range(len(nums)-1, -1, -1):
            print()
            print(f'ind: {ind}')
            print(f'before')
            print(f'vold: {vold} s1: {s1} s2: {s2}')
            vnew = nums[ind] + max([s1, s2])
            s2 = s1
            s1 = vold
            vold = vnew
            print(f'after')
            print(f'vnew: {vnew} vold: {vold} s1: {s1} s2: {s2}')

        return max([vnew, s1])


if __name__ == "__main__":

    nums = [5,4,10,5,4,10,1,10,5]
    nums = [1,2]

    sol = Solution()
    print(sol.rob(nums))
