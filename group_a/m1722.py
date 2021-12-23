# 1722. Minimize Hamming Distance After Swap Operations
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

from collections import Counter
from copy import deepcopy


class Solution:
    # def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
    def minimumHammingDistance(self, source, target, allowedSwaps):

        if not source:
            return 0

        if not allowedSwaps:
            return sum([1 for ii in range(len(source)) if source[ii]!= target[ii]])

        def dfs(val, paths, current_tree, inds):
            # current_tree.add(val)
            current_tree.append(val)
            inds.discard(val)

            # for child in paths.get(val, set()):
            if paths.get(val):
                children = paths.pop(val)
            else:
                return

            for child in children:
                # paths[child].discard(val)
                if child != val and child in inds:
                    dfs(child, paths, current_tree, inds)

        n = len(source)

        paths = {x: set() for x in range(n)}
        inds = set(range(n))
        hammingDistance = 0

        for a,b in allowedSwaps:
            paths[a].add(b)
            paths[b].add(a)

        while inds:
        # while paths:
            val = inds.pop()
            # current_path = set()
            current_path = list()
            dfs(val, paths, current_path, inds)

            c1 = Counter([source[x] for x in current_path])
            c2 = Counter([target[x] for x in current_path])
            hammingDistance += sum((c1 - c2).values())

        return hammingDistance





if __name__ == "__main__":
    source = [1,2,3,4];
    target = [2,1,4,5]
    allowedSwaps = [[0,1],[2,3]]

    sol = Solution()
    print(sol.minimumHammingDistance(source, target, allowedSwaps))


