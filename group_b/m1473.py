
import itertools
from collections import defaultdict

class Solution:
    # def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
    def minCost(self, houses, cost, m, n, target):

        def generate_combinations(houses, num_houses, num_colors, seen_houses, last_color, target):
            if len(seen_houses.keys()) >= target:
                # return f"best{num_houses}"
                return last_color
            pass

        color_schemes = list(itertools.permutations(range(1, n+1)))
        memo = {scheme: dict() for scheme in color_schemes}

        last_known_color = 0
        seen_houses = defaultdict(int)

        for ii, house_color in enumerate(houses):
            if house_color != 0:
                seen_houses[house_color] += 1
                last_known_color = house_color
                continue

            possible_combinations = generate_combinations(houses, num_houses=ii, num_colors=min(n, ii + 1), seen_houses=seen_houses, last_color=last_known_color, target)
        pass


if __name__ == "__main__":

    houses = [0,0,0,0,0]
    cost = [[1,10],[10,1],[10,1],[1,10],[5,1]] 
    m = 5
    n = 2
    target = 3

    sol = Solution()
    print(sol.minCost(houses, cost, m, n, target))
