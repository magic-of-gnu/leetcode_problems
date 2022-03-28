import heapq

class Solution:

    def minSteps(self,n):

        if n == 1:
            return 0

        q = []
        heapq.heappush(q, (-1,1,1))
        result = [float('inf')]

        while q:

            c += 1

            state = heapq.heappop(q)
            nchar, curr_n, count = -state[0], state[1], state[2]

            if curr_n == n:
                result[0] = min(result[0], count)

            if count > result[0] or curr_n > n:
                continue

            heapq.heappush(q, (-nchar, curr_n+nchar, count+1))

            if n % curr_n == 0 and curr_n != nchar:
                heapq.heappush(q, (-curr_n, curr_n, count+1))

        return result[0]


if __name__ == "__main__":

    # a   
    # aa   CP
    # aaa  CPP

    n = 3
    output = 3

    n = 4
    output = 4

    n = 10
    output = 7

    n = 30
    output = 10

    n = 100
    output = 14

    sol = Solution()
    print(sol.minSteps(n))
