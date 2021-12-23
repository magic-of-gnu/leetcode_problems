# 1870. Minimum Speed to Arrive on Time

# You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

# Each train can only depart at an integer hour, so you may need to wait in between each train ride.
# 
#     For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
# 
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.
# 
# Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

import math

class Solution:
    # def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
    def minSpeedOnTime(self, dist, hour):


        def calculate_total_time(dist, vel):
            t = 0
            for x in dist:
                t = math.ceil(t) + x / vel

            return t

        n = len(dist)
        if n > math.ceil(hour):
            print('ddd')
            return -1

        total_dist = sum(dist)
        vel = math.ceil(total_dist/hour)
        vel_old = vel

        # find the range via log grid search
        while True:
            t = calculate_total_time(dist, vel)

            if t <= hour:
                break

            if vel == 1:
                vel = 2
            else:
                vel_old = vel
                vel = vel**2

        # print(f'vel_old: {vel_old} vel: {vel}')
        if vel == vel_old:
            return vel

        # find the value in the range of [vel, vel**2] via binary search
        low = vel_old
        high = vel
        mid = int(low + (high - low) / 2)

        _low, _mid, _high = -1, -2, -3

        ii = 0
        _t = 0

        while True:

            if _low == _mid == _high:
                break
            _low, _mid, _high = low, mid, high
            t = calculate_total_time(dist, mid)

            # print()
            # print(f'low: {low} mid: {mid} high: {high}')
            # print(f'mid: {mid} t: {t}')

            if t > hour:
                low = mid + 1
            elif t < hour:
                high = mid - 1
            elif t == hour:
                return mid

            if t <= hour:
                if t > _t:
                    _t = t
                    min_speed = mid

            mid = int(low + (high-low) / 2)

            # if ii > 10:
            #     break
            ii += 1

        return min_speed


if __name__ == "__main__":
    dist = [1,3,2]; hour = 6

    dist = [3,4,5]; hour = 2

    dist = [3,4,5]; hour = 2.01

    dist = [1,3,2]; hour = 2.7

    dist = [5,3,4,6,2,2,7]; hour = 10.92

    dist = [1,1,100000]; hour = 2.01

    dist = [92,41,28,84,64,51,83,59,19,34,18,32,96,72,69,34,96,75,55,75,52,47,29,18,66,64,12,97,7,15,20,81,21,88,55,77,9,50,49,77,60,68,33,71,2,88,93,15,88,69,97,35,99,83,44,15,38,56,21,59,1,93,93,34,65,98,23,65,14,81,39,82,65,78,26,20,48,98,21,70,100,68,1,77,42,63]
    hour = 107.52




    sol = Solution()
    print(sol.minSpeedOnTime(dist, hour))
