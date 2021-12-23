class Solution:
    def longestOnes(self, nums, k: int) -> int:

        # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; 
        n = len(nums)

        left, right = 0, 0
        count = 0
        max_count = 0
        curr_k = k # 3


        while right < n:
            # print()
            # print(f'left: {left} right: {right} num: {nums[right]}')
            # print(f'count: {count} max_count: {max_count}')
            # print(f'curr_k: {curr_k}')

            if nums[right] == 1:
                right += 1
                count += 1
                max_count = max(max_count, count)

                if k == 0:
                    left += 1

            elif nums[right] == 0:

                if k == 0:
                    left += 1
                    right += 1
                    count = 0

                elif k != 0 and curr_k > 0:
                    right += 1
                    count += 1
                    max_count = max(max_count, count)
                    curr_k -= 1
                elif k!= 0 and curr_k == 0:
                    while curr_k == 0 and left < right:
                        if nums[left] == 0:
                            curr_k += 1

                        left += 1
                        count -= 1

            # print(f'left: {left} right: {right}')
            # print(f'count: {count} max_count: {max_count}')
            # print(f'curr_k: {curr_k}')

        return max_count



if __name__ == "__main__":
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; 
    k = 3
    output = 10

    nums = [0,0,1,1,1,0,0]
    k = 0

    # nums = [1,0,1,0,1,1]
    # k = 0
    # output = 4

    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 0

    sol = Solution()
    print(sol.longestOnes(nums, k))
