from collections import Counter
from itertools import permutations

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        nlen = len(str(n+1))

        def generate_balanced_number2(d0, nlen):
            # d0 starting int
            # nlen total length to generate

            num0 = int(str(d0) * d0)

            if len(str(num0)) > nlen:
                return False

            nrem = nlen - d0

            results = []

            for starting_digit in range(d0+1, 10):
                vrem = generate_balanced_number(starting_digit, nrem)
                if vrem[0] is not False:
                    results.append(int(str(num0) + vrem[1]))

            return results


        def generate_balanced_number(d0, nlen):
            # d0 starting int
            # nlen total length to generate

            num0 = int(str(d0) * d0)

            if len(str(num0)) > nlen:
                return False

            nrem = nlen - d0

            results = []

            for starting_digit in range(d0+1, 10):
                vrem = generate_balanced_number(starting_digit, nrem)
                if vrem[0] is not False:
                    results.append(int(str(num0) + vrem[1]))

            return results


        a = generate_balanced_number(1,4)
        print(a)


    def nextBeautifulNumber(self, n: int) -> int:

        def generate_num(prev_num, digit, nlen, results):

            prev_num = prev_num + str(digit)*digit
            if len(prev_num) > nlen:
                return False

            elif len(prev_num) == nlen:

                print(f'adding; prev_num: {prev_num} n: {n}')

                found = False
                for perm in permutations(prev_num):
                    perm = int(''.join(perm))
                    if perm > n:
                        if not results:
                            results.append(perm)

                        results[0] = min(results[0], perm)

                # if found is True:
                #     results.add(min_num)

                return True

            for d in range(digit+1, 10):
                num = generate_num(prev_num, d, nlen, results)
                # if results:
                #     break

                if num is False:
                    break
                
            return True

        nums = []
        nlen = len(str(n))

        while not nums:
            num = generate_num('', 0, nlen, nums)
            nlen += 1

        return nums.pop()








if __name__ == "__main__":
    n = 3000
    Output = 3133

    n = 9999
    n = 16407; output = 22333

    sol = Solution()
    print(sol.nextBeautifulNumber(n))
