# 1375. Bulb Switcher III

# There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

# At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.
# 
# Return the number of moments in which all turned on bulbs are blue.

class Solution:
    def numTimesAllBlue(self, lights):
        if not lights:
            return 0


        n = len(lights)
        count_all_blue = 0
        last_blue_pos = -1

        for ii in range(n):
            lights[(lights[ii]%n)-1] += n

            for l in range(last_blue_pos+1, n):
                if lights[l] > n:
                    last_blue_pos = l
                else:
                    break

            if last_blue_pos == ii:
                count_all_blue += 1

        return count_all_blue

if __name__ == "__main__":
    lights = [0, 1, 2, 3]
    Output = 4

    lights = [3, 2, 1, 0]
    Output = 1

    lights = [2,1,3,5,4]
    Output = 3

    sol = Solution()
    print(sol.numTimesAllBlue(lights))
