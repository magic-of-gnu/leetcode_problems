# 1503. Last Moment Before All Ants Fall Out of a Plank

# We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with speed 1 unit per second. Some of the ants move to the left, the other move to the right.

# When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions doesn't take any additional time.
# 
# When an ant reaches one end of the plank at a time t, it falls out of the plank imediately.
# 
# Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right. Return the moment when the last ant(s) fall out of the plank.

from pprint import pprint as pp

class Solution:
    # def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    def getLastMoment(self, n, left, right):
        max_left = max(left)
        max_right = n - min(right)
        return max(max_left, max_right)

if __name__ == "__main__":
    n = 4; left = [4,3]; right = [0,1]
    # n = 6; left = [1, 2]; right = [0, 3]
    # n = 6; left = [5, 4]; right = [0, 1]

    sol = Solution()
    print(sol.getLastMoment(n, left, right))

