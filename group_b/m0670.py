# 670. Maximum Swap

# You are given an integer num. You can swap two digits at most once to get the maximum valued number.

# Return the maximum valued number you can get.

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num


        snum = [int(x) for x in str(num)]
        n = len(snum)
        ind_at_change = n + 1
        val_large = _val_large = 0
        ind_val = n + 1

        for ind, val in enumerate(snum[1:], start=1):

            if snum[ind] != snum[ind-1]:
                ind_at_change = min(ind_at_change, ind)

            if ind_at_change < n + 1:

                _val_large = max(val_large, val)
                if _val_large != val_large:
                    ind_val = ind
                    val_large = _val_large

            print(f'ind: {ind} val: {val}')
            print(f'snum[ind]: {snum[ind]} snum[ind-1]: {snum[ind-1]}')
            print(f'ind_at_change: {ind_at_change}')
            print(f'val_large: {val_large} ind_val: {ind_val}')

        if ind_val > n:
            return num

        if ind_val == ind_at_change and snum[0] > snum[ind_at_change]:
            return num

        if val_large > snum[ind_at_change-1]:
            print('here')
            a = ''.join([str(x) for x in [val_large] + snum[1:ind_val] + [snum[0]] + snum[ind_val+1:]])
        else:
            print('there')
            a = ''.join([str(x) for x in snum[:ind_at_change] + [val_large] + snum[ind_at_change+1:ind] + [snum[ind_at_change]] + snum[ind_val+1:]])

        return int(a)


if __name__ == "__main__":
    # n = 9987
    # n = 1234
    n = 9989
    n = 2736

    n = 10
    n = 11
    
    n = 98368

    sol = Solution()
    print(sol.maximumSwap(n))
