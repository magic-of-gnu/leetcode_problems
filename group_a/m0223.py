class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        m1 = max(ax1, bx1)
        n1 = max(ay1, by1)

        m2 = min(ax2, bx2)
        n2 = min(ay2, by2)

        if m1 > m2 or n1 > n2:
            intersection = 0
        else:
            intersection = (m2-m1)*(n2-n1)


        return (ax2-ax1)*(ay2-ay1) + \
               (bx2-bx1)*(by2-by1) - \
               intersection



if __name__ == "__main__":

    ax1 = -3; ay1 = 0; ax2 = 3; ay2 = 4; bx1 = 0; by1 = -1; bx2 = 9; by2 = 2

    sol = Solution()
    print(sol.computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2))
