class Solution:
    def singleNumber(self, nums):
        s = 0
        for num in nums:
            s ^= num

        last_bit = s & (s-1) ^ s
        num1 = s
        
        for num in nums:
            if last_bit & num != 0:
                num1 ^= num

        num2 = s ^ num1

        return num1, num2





if __name__ == '__main__':
    nums = [1,2,1,3,2,5]
    nums = [1,2,1,-3,2,-5]

    sol = Solution()
    print(sol.singleNumber(nums))
