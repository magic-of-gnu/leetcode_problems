import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations):

        possible_fuel = []
        result = 0

        current_fuel = startFuel # 0

        start_ind, ind = 0, 0
        n = len(stations)    # 4

        # [[10,60],[30,5],[50,20],[60,5]]
        # target = 100, startFuel = 30

        while ind < n and current_fuel < target:

            # ind = start_ind

            print()
            print(f'ind: {ind} current_fuel: {current_fuel}')
            while ind < n and current_fuel >= stations[ind][0]:

                print(f'ind: {ind} current_fuel: {current_fuel} possible_fuel: {possible_fuel}')
                heapq.heappush(possible_fuel, -stations[ind][1])
                ind += 1 # 1, 2, 3, 4

            print(f'start_ind: {start_ind}')
            print(f'possible_fuel: {possible_fuel}')

            if len(possible_fuel) == 0:
                break

            result += 1  # 2
            popped = heapq.heappop(possible_fuel)
            current_fuel = current_fuel-popped  # 90, 110
            # start_ind = max(popped[1] + 1, start_ind)
            # start_ind = ind + 1

            print(f'new current_fuel: {current_fuel}')
            print(f'result: {result}')

        if current_fuel >= target:
            return result

        return -1
        

if __name__ == "__main__":
    target = 100; startFuel = 30; stations = [[10,60],[30,5],[50,20],[60,5]]


    target = 1000; 
    startFuel = 299; 
    #              0        1        2        3         4         5         6         7 
    stations = [[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]


    # target = 100; startFuel = 1; stations = [[10,100]]

    target = 1000; startFuel = 83; stations = [[25,27],[36,187],[140,186],[378,6],[492,202],[517,89],[579,234],[673,86],[808,53],[954,49]]


    sol = Solution()
    print(sol.minRefuelStops(target, startFuel, stations))



