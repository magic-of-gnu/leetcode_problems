from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product

class Solution:
    def numOfWays(self, n: int) -> int:
        def create_valid_combs(arr, k):
            combs = list(product('reg',repeat=k))
            valid_combs = []

            for comb in combs:
                is_valid = True
                for ii in range(1,k):
                    if comb[ii] == comb[ii-1]:
                        is_valid = False
                        break

                if is_valid is True:
                    valid_combs.append(comb)

            return valid_combs

        def create_states_memo(valid_combs, k):

            states = dict()
            memo = dict()

            for a in valid_combs:
                valid_children = []
                for b in valid_combs:
                    is_valid = True
                    if a[0] == b[0]:
                        is_valid = False

                    for ii in range(1,k):
                        if a[ii] == b[ii] or b[ii] == b[ii-1]:
                            is_valid = False
                            break

                    if is_valid is True:
                        valid_children.append(b)

                states[a] = valid_children
                memo[a] = len(valid_children)

            return states, memo

        k = 3
        valid_combs = create_valid_combs('reg', k)

        if n == 1:
            return len(valid_combs)

        states, memo = create_states_memo(valid_combs, k)

        for ii in range(3,n+1):
            new_memo = dict()
            for state, children in states.items():
                s = 0
                for child in children:
                    s += memo[child]

                new_memo[state] = s

            memo = new_memo

        return sum(memo.values()) % (10**9+7)


if __name__ == "__main__":
    n = 2
    n = 3
    n = 7
    n = 5000

    sol = Solution()
    print(sol.numOfWays(n))
