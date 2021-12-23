# 970. Powerful Integers

# Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

# An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

# You may return the answer in any order. In your answer, each value should occur at most once.

import math

class Solution:
    # def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
    def powerfulIntegers(self, x, y, bound):

        if bound < 2:
            return []

        if bound == 2:
            return [2]

        imax = int(math.log(bound-1, x)) + 1 if x != 1 else 1
        jmax = int(math.log(bound-1, y)) + 1 if y != 1 else 1

        results = dict()
        print(f'imax: {imax} jmax: {jmax}')

        for ii in range(imax+1):
            for jj in range(jmax+1):
                s = x**ii + y**jj
                # print()
                # print(f'ii: {ii} jj: {jj} s: {s} bound: {bound}')
                if s > bound:
                    break
                results[s] = 1

        return list(results.keys())
        


if __name__ == "__main__":
    x = 2; y = 3; bound = 10
    Output = [2,3,4,5,7,9,10]

    x = 1; y = 1; bound = 5
    x = 2; y = 2; bound = 5

    x = 60; y = 56; bound = 175617

    sol = Solution()
    print(sol.powerfulIntegers(x, y, bound))
