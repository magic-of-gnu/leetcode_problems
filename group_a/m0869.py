# 869. Reordered Power of 2

# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        def get_counter(n):
            counter = {x: 0 for x in range(10)}

            for x in str(n):
                counter[int(x)] += 1

            return counter, sum(counter.values())

        n_counter, n_num_digits = get_counter(n)

        x = 0

        while True:
            p2 = 2**x
            x += 1
            p_counter, p_num_digits = get_counter(p2)

            if p_num_digits > n_num_digits:
                return False
            elif n_num_digits > p_num_digits:
                continue

            is_power2 = True

            for digit in range(10):
                if n_counter[digit] != p_counter[digit]:
                    is_power2 = False
                    break

            if is_power2 is True:
                return True


if __name__ == "__main__":
    n = 1
    Output = True

    n = 23678
    Output = True
    
    n = 23679
    Output = True

    sol = Solution()
    print(sol.reorderedPowerOf2(n))
