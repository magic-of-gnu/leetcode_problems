import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes):

        def get_min(values):
            min_value = min(values)
            return [ind for ind in range(len(values)) if min_value == values[ind]]

        # time: O(nlogn), space: O(k), k = len(primes)
        if n == 1:
            return 1

        if len(primes) == 1:
            return primes[0]**(n-1)

        inds = [0] * len(primes)
        values = [x for x in primes]
        result = [1]

        for ii in range(n-1):
            min_inds = get_min(values)
            result.append(values[min_inds[0]])
            for ind in min_inds:
                inds[ind] += 1
                values[ind] = primes[ind] * result[inds[ind]]

        return result[-1]


    def nthSuperUglyNumber(self, n, primes):
	    cand = [(p, p, 1) for p in primes]
	    ugly = [1]
	    for _ in range(n-1):
	    	ugly.append(cand[0][0])
	    	while cand[0][0] == ugly[-1]:
	    		x, p, i = heapq.heappop(cand)
	    		heapq.heappush(cand, (p*ugly[i], p, i+1))
	    return ugly[-1]


if __name__ == "__main__":
    primes = [2,7,13,19]
    n = 12

    n = 15
    primes = [3,5,7,11,19,23,29,41,43,47]

    sol = Solution()
    print(sol.nthSuperUglyNumber(n, primes))
