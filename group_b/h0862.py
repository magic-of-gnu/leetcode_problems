class Solution:
    def shortestSubarray(self, nums, k: int) -> int:

        n = len(nums)

        left = 0
        min_length = n

        s = 0

        for right in range(n):
            print()
            print(f'left: {left} right: {right} min_length: {min_length}')
            print(f'val.left: {nums[left]} val.right: {nums[right]}')
            print(f's: {s}')
            s += nums[right]
            print('after')
            print(f's: {s}')

            while s >= k and left <= right:
                print(f'update')
                min_length = min(min_length, right-left+1)
                print(f'min_length: {min_length}')
                s -= nums[left]
                print(f'new s: {s}')

        return min_length


if __name__ == "__main__":
    nums = [2,-1,2,3]; k = 3

    sol = Solution()
    print(sol.shortestSubarray(nums, k))
