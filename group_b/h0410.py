
class Solution:

    def splitArray(self, nums, m):

        if len(nums) == m:
            return max(nums)

        def get_sum(prefix_sum, start, end):
            return prefix_sum[end] - prefix_sum[start]

        def split_into_two_groups(prefix_sum, start, end, ngroups, memo):
            print()
            print(f'before start: {start}, end: {end} ngroups: {ngroups}')

            if ngroups == 1:
                print(f'exiting at ngroups == 1')
                return get_sum(prefix_sum, start, end)

            elif ngroups == 2:
                print(f'exiting at ngroups == 2')

                if (start, end, ngroups) in memo:
                    # print(f'(start, end) in memo; memo[({start}, {end})] = {memo[(start, end)]}')
                    return memo[(start, end, ngroups)]

                print(f'values not in memo, start, end: ({start}, {end})')

                max_sums = []

                for ii in range(start+1, end):
                    print(f'ngroups==2, gr1 start: {start} end: {ii}')
                    print(f'ngroups==2, gr2 start: {ii} end: {end}')
                    v1 = get_sum(prefix_sum, start,  ii)
                    v2 = get_sum(prefix_sum,    ii, end)

                    print(f'v1: {v1} v2: {v2}')
                    max_sum = max(get_sum(prefix_sum, start,  ii),
                                  get_sum(prefix_sum,    ii, end)
                                 )
                    max_sums.append(max_sum)

                memo[(start, end, ngroups)] = min(max_sums)

                return memo[(start, end, ngroups)]
            
            elif ngroups > 2:

                if (start, end, ngroups) in memo:
                    return memo[(start, end, ngroups)]

                max_sums = []
                for ii in range(start+1, end-(ngroups-2)):
                    gr = [start, ii]
                    gr_sum = get_sum(prefix_sum, start, ii)
                    print(f'ngroups>2, start: {ii} end: {end} gr.start: {start} gr.end: {ii} gr_sum: {gr_sum}')
                    rem_sum = split_into_two_groups(prefix_sum, ii, end, ngroups-1, memo)
                    print(f'gr_sum: {gr_sum} rem_sum: {rem_sum}')
                    max_sums.append(max(gr_sum, rem_sum))

                memo[(start, end, ngroups)] = min(max_sums)

                return memo[(start, end, ngroups)]


        n = len(nums)
        prefix_sum = [0]

        for num in nums:
            # if num != 0:
            prefix_sum.append(prefix_sum[-1] + num)

        memo = dict() # key: range for the last two groups; value: minimum max_sum
        # print(prefix_sum)

        min_sum = split_into_two_groups(prefix_sum, 0, len(prefix_sum)-1, m, memo)


        return min_sum


    def splitArray(self, nums, m):

        if len(nums) == m:
            return max(nums)

        def get_sum(prefix_sum, start, end):
            return prefix_sum[end] - prefix_sum[start]

        def split_into_two_groups(prefix_sum, start, end, ngroups, memo):
            print()
            print(f'before start: {start}, end: {end} ngroups: {ngroups}')

            if ngroups == 1:
                print(f'exiting at ngroups == 1')
                return get_sum(prefix_sum, start, end)

            elif ngroups == 2:
                print(f'exiting at ngroups == 2')

                if (start, end, ngroups) in memo:
                    # print(f'(start, end) in memo; memo[({start}, {end})] = {memo[(start, end)]}')
                    return memo[(start, end, ngroups)]

                print(f'values not in memo, start, end: ({start}, {end})')

                max_sums = []

                for ii in range(start+1, end):
                    print(f'ngroups==2, gr1 start: {start} end: {ii}')
                    print(f'ngroups==2, gr2 start: {ii} end: {end}')
                    v1 = get_sum(prefix_sum, start,  ii)
                    v2 = get_sum(prefix_sum,    ii, end)

                    print(f'v1: {v1} v2: {v2}')
                    max_sum = max(get_sum(prefix_sum, start,  ii),
                                  get_sum(prefix_sum,    ii, end)
                                 )
                    max_sums.append(max_sum)

                memo[(start, end, ngroups)] = min(max_sums)

                return memo[(start, end, ngroups)]
            
            elif ngroups > 2:

                if (start, end, ngroups) in memo:
                    return memo[(start, end, ngroups)]

                max_sums = []
                for ii in range(start+1, end-(ngroups-2)):
                    gr = [start, ii]
                    gr_sum = get_sum(prefix_sum, start, ii)
                    print(f'ngroups>2, start: {ii} end: {end} gr.start: {start} gr.end: {ii} gr_sum: {gr_sum}')
                    rem_sum = split_into_two_groups(prefix_sum, ii, end, ngroups-1, memo)
                    print(f'gr_sum: {gr_sum} rem_sum: {rem_sum}')
                    max_sums.append(max(gr_sum, rem_sum))

                memo[(start, end, ngroups)] = min(max_sums)

                return memo[(start, end, ngroups)]


        n = len(nums)
        prefix_sum = [0] * (n+1)

        for ii in range(n):
            prefix_sum[ii+1] = prefix_sum[ii] + nums[ii]

        memo = dict() # key: range for the last two groups; value: minimum max_sum

        for ii in range(1, len(prefix_sum) - 1):
            gr1_sum = get_sum(prefix_sum, 0, ii)
            gr2_sum = get_sum(prefix_sum, ii, n)

            memo[(0,n, 2)] = min(memo.get((0,n,2), float('inf')), max(gr1_sum, gr2_sum))

        min_sum = split_into_two_groups(prefix_sum, 0, len(prefix_sum)-1, m, memo)


        return min_sum



if __name__ == "__main__":

    nums = [7,2,5,10,8];
    m = 2

    nums = [7,2,5,10,8];
    m = 3

    nums = [7,2,5,10,8] + [7,2,5,10,8];
    m = 4

    nums = [2,3,1,2,4,3]
    m = 5

    nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,250,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,350,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,400,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,450,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,500,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,550,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,600,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,650,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,700,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,750,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,800,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,850,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,900,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,950,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    m = 50


    sol = Solution()
    print(sol.splitArray(nums, m))

