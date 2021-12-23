from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:

        def add_window_counter(window_counter, num, nuniq):
            if num in window_counter:
                window_counter[num] += 1
            else:
                window_counter[num] = 1
                nuniq += 1

            return window_counter, nuniq


        def rem_window_counter(window_counter, num, nuniq):
            window_counter[num] -= 1

            if window_counter[num] == 0:
                window_counter.pop(num)
                nuniq -= 1

            return window_counter, nuniq


        def move_left_till_target(nums, left, right, window_counter, nuniq, k):

            while nuniq > k and left <= right:
                window_counter, nuniq = rem_window_counter(window_counter, nums[left], nuniq)
                left += 1

            return window_counter, nuniq, left


        def count_subarrays_till_k(nums, k):

            n = len(nums)
            leftk, leftp = 0, 0
            windowk, windowp = dict(), dict()
            countk, countp = [0]*(n+1), [0]*(n+1)
            nuniqk, nuniqp = 0, 0
            currnk, currnp = 0, 0

            for right in range(n):
                # print()
                # print(f'before')
                # print(f'leftk: {leftk} leftp: {leftp} right: {right}')
                # print(f'nuniqk: {nuniqk} nuniqp: {nuniqp}')
                # print(f'windowk: {windowk} windowp: {windowp}')
                # print(f'countk: {countk} countp: {countp}')

                windowk, nuniqk = add_window_counter(windowk, nums[right], nuniqk)
                windowp, nuniqp = add_window_counter(windowp, nums[right], nuniqp)

                # print(f'mid')
                # print(f'leftk: {leftk} leftp: {leftp} right: {right}')
                # print(f'nuniqk: {nuniqk} nuniqp: {nuniqp}')
                # print(f'windowk: {windowk} windowp: {windowp}')

                if nuniqk > k:
                    windowk, nuniqk, leftk = \
                        move_left_till_target(nums, leftk, right, windowk, nuniqk, k)

                    currnk = right + 1 - leftk

                else: # nuniqk == k:
                    currnk = currnk + 1

                if nuniqp > k-1:
                    windowp, nuniqp, leftp = \
                        move_left_till_target(nums, leftp, right, windowp, nuniqp, k-1)

                    currnp = right + 1 - leftp
                else: # nuniqp == k-1:
                    currnp = currnp + 1

                countk[right+1] = countk[right] + currnk
                countp[right+1] = countp[right] +  currnp

                # print(f'after')
                # print(f'leftk: {leftk} leftp: {leftp} right: {right}')
                # print(f'nuniqk: {nuniqk} nuniqp: {nuniqp}')
                # print(f'windowk: {windowk} windowp: {windowp}')
                # print(f'countk: {countk} countp: {countp}')

            return countk[-1] - countp[-1]

        return count_subarrays_till_k(nums, k)



if __name__ == "__main__":
     nums = [1,1,1,2,1,3,1,2,3,4]
     k = 3
        
     sol = Solution()
     print(sol.subarraysWithKDistinct(nums, k))
