import heapq

class Solution:
    def nthUglyNumber2(self, n: int) -> int:

        if n == 1:
            return 1

        nums = {1: 1}
        count = 1
        muls = [2, 3, 5]
        ii = 1

        while count != n:

            ii += 1
            for mul in muls:
                val, rem = ii // mul, ii % mul     # 1, 0

                if rem == 0 and nums.get(val, 0) == 1:
                    nums[ii] = 1
                    count += 1
                    break

        return ii

    def nthUglyNumber(self, n: int) -> int:

        if n == 1:
            return 1

        muls = [2, 3, 5]
        count = 1
        seen = set()

        q = []

        heapq.heappush(q, 2)
        heapq.heappush(q, 3)
        heapq.heappush(q, 5)

        while True:
            count += 1
            val = heapq.heappop(q)

            if count == n:
                break

            for mul in muls:
                if val * mul not in seen:
                    heapq.heappush(q, val*mul)
                    seen.add(val*mul)

        return val


if __name__ == "__main__":

    n = 25
    n = 10
    n = 12
    n = 2

    n = 400

    sol = Solution()
    print(n,sol.nthUglyNumber(n))
    # [print(n,sol.nthUglyNumber(n)) for n in [1,2,3,4,5,6,7,8,9,10,15]]

