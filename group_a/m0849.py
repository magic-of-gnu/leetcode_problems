
class Solution:
    def maxDistToClosest(self, seats):
        left, right = 0, 0
        max_len = -1
        result = None
        n = len(seats)
    
        for right in range(n):
            if right == n - 1:
                 if seats[right] == 0:
                     # right end
                     if right - left > max_len:
                         max_len = right - left
                     continue
            if seats[right] == 1:
                if left == 0 and seats[left] == 0:
                    # left end
                    if right - left > max_len:
                         max_len = right - left
                    left = right
                    continue
    
                if (right - left)//2 > max_len:
                    max_len = (right - left)//2

                left = right

        return max_len
    

if __name__ == "__main__":
    # seats = [0,0,0,1,0,0,1]
    # seats = [0,0,0,1,0,0,1,0,0,0,0,0]
    # seats = [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0]
    # seats = [0,1]
    seats = [1,0]

    sol = Solution()
    print(sol.maxDistToClosest(seats))
