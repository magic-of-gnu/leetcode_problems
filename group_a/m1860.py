# 1860. Incremental Memory Leak

# You are given two integers memory1 and memory2 representing the available memory in bits on two memory sticks. There is currently a faulty program running that consumes an increasing amount of memory every second.
# 
# At the ith second (starting from 1), i bits of memory are allocated to the stick with more available memory (or from the first memory stick if both have the same available memory). If neither stick has at least i bits of available memory, the program crashes.
# 
# Return an array containing [crashTime, memory1crash, memory2crash], where crashTime is the time (in seconds) when the program crashed and memory1crash and memory2crash are the available bits of memory in the first and second sticks respectively.

# 24 June 2021

import math

class Solution:
    # def memLeak(self, memory1: int, memory2: int) -> List[int]:
    def memLeak(self, m1, m2):
        
        def solve_q(a, b, c):
            # solve quadratic equation, get higher value, and return ceil and floor
            # ax2 + bx + c = 0
            x = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)

            return math.ceil(x), math.floor(x)

        def sum_arithmetic_series(a1, d, n):
            return int((a1 + a1 + (n-1)*d) / 2 * n)

        def get_sum_from_approx_sum(a1, d, approx_sum, original_sum):
            # a = d
            # b = 2*a1 - d
            # c = -2*approx_sum

            nh, nl = solve_q(d, 2*a1 - d, -2*approx_sum)

            sh, sl = sum_arithmetic_series(a1, d, nh), sum_arithmetic_series(a1, d, nl)

            return original_sum - sl, original_sum - sh, nl, nh

        case = -1
        count = 0

        if m1 > m2:
            rem_lower, rem_higher, n_lower, n_higher = get_sum_from_approx_sum(1, 1, abs(m1-m2), m1)
            left_mem = m2
            case = 1
        elif m1 < m2:
            rem_lower, rem_higher, n_lower, n_higher = get_sum_from_approx_sum(1, 1, abs(m1-m2), m2)
            left_mem = m1
            case = 2
        else: # m1 == m2:
            rem_lower, rem_higher, n_lower, n_higher = get_sum_from_approx_sum(1, 1, 1 , m1)
            left_mem = m2
            case = 1

        if rem_higher >= 0:
            rem_mem = rem_higher
            n_mem = n_higher
        elif rem_higher < 0:
            rem_mem = rem_lower
            n_mem = n_lower

        count += n_mem

        if rem_mem == left_mem:
            case = 2

        mem1, mem2 = left_mem, rem_mem

        rem_lower1, rem_higher1, n_lower1, n_higher1 = get_sum_from_approx_sum(n_mem + 1, 2, mem1, mem1)
        rem_lower2, rem_higher2, n_lower2, n_higher2 = get_sum_from_approx_sum(n_mem + 2, 2, mem2, mem2)

        count += 2*min(n_lower1, n_lower2) + abs(n_lower1-n_lower2) + 1

        if case == 1:
            return count, rem_lower2, rem_lower1
        if case == 2:
            return count, rem_lower1, rem_lower2




if __name__ == "__main__":
    memory1 = 2; memory2 = 2
    memory1, memory2 = 12, 20
    # memory1, memory2 = 2, 2
    memory1, memory2 = 8, 11
    # memory1, memory2 = 1, 1
    memory1, memory2 = 5, 7

    sol = Solution()
    print(sol.memLeak(memory1, memory2))
