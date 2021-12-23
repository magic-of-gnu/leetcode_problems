class Solution:

    def carFleet(self, target: int, position, speed) -> int:

        def sort_position_speed(position, speed):
            inds = sorted(range(n), key=lambda x: position[x])
            position = [position[x] for x in inds]
            speed = [speed[x] for x in inds]
    
            return position, speed

        n = len(position)

        position, speed = sort_position_speed(position, speed)

        st = []
        next_car_fleet = [0]*n

        last_time, time, num_fleets = -1, 0, 0

        for ii in reversed(range(n)):
            time = (target - position[ii]) / speed[ii]
            if last_time < time:
                last_time = time
                num_fleets += 1

        return num_fleets


if __name__ == "__main__":
    target = 12; position = [10,8,0,5,3]; speed = [2,4,1,1,3]

    sol = Solution()
    print(sol.carFleet(target, position, speed))
