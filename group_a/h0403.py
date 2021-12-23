class Solution:
    def canCross(self, stones) -> bool:

        n = stones[-1]

        def dfs(arr, seen, pos, k):    # arr, 1, 1;   arr, 3, 2
            if not (0 <= pos <= n):
                return False

            if pos not in arr:   # {0,1,3,5,6,8,12,17}
                return False

            if (pos, k) in seen:
                return False

            if pos == n:
                return True

            for newk in [k-1, k, k+1]:  # 1, 2, 3
                new_pos = pos + newk    # 3 + 2
                if new_pos < pos + 1:   # 5 < 2
                    continue

                if dfs(arr, seen, new_pos, newk):  # arr, 5, 2
                    return True

            seen.add((pos,k))

            return False

        arr = {val:ind for ind, val in enumerate(stones)}
        memo = set()

        return dfs(arr, memo, 1, 1)


if __name__ == "__main__":

    stones = [0,1,3,5,6,8,12,17]
    output = True

    sol = Solution()
    print(sol.canCross(stones))

