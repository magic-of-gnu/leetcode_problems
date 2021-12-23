# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

# You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:
# 
#     horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
#     verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
# 
# Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

# 2021 June 08

class Solution:
    # def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    def maxArea(self, h, w, horizontalCuts, verticalCuts):

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        height = 0
        width = 0
        x_prev = 0

        for x in horizontalCuts + [h]:
            height = max(height, x - x_prev)
            x_prev = x

        x_prev = 0
        for x in verticalCuts + [w]:
            width = max(width, x - x_prev)
            x_prev = x

        return (height * width) % (10**9 + 7)


if __name__ == "__main__":
    h = 5; w = 4; horizontalCuts = [1,2,4]; verticalCuts = [1,3]
    Output = 4 

    h = 5
    w = 4
    horizontalCuts = [3,1]
    verticalCuts = [1]


    h = 6
    w = 3
    horizontalCuts = [5,4,1,2,3]
    verticalCuts = [2,1]

    sol = Solution()
    print(sol.maxArea(h, w, horizontalCuts, verticalCuts))
