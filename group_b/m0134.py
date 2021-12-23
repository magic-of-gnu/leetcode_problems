class Solution:
    def canCompleteCircuit(self, gas, cost):
        results = dict()
        n = len(gas)

        for ii in range(n-1, -1, -1):                # (0, 1)
            current_gas = 0
            jj = ii
            count = 0

            # print()
            # print()


            while True:                              # 0


                jj = jj % n
                # print()
                # print(f'ii: {ii} jj: {jj}')
                # print(f'results: {results}')
                # print(f'current_gas: {current_gas}')
                _current_gas = (gas[jj] - cost[jj])  # 1 - 3 = -2
                # print(f'_current_gas: {_current_gas}')
                count += 1

                if count == n:
                    if current_gas + _current_gas >= 0:
                        return ii
                    break

                if current_gas + _current_gas >= 0:
                    current_gas += _current_gas
                    if jj + 1 in results:
                        # print(f'jj: {jj}')
                        # print(results)
                        current_gas += results[jj+1][1]
                        jj = results[jj+1][0]
                    else:
                        jj += 1
                else:
                    results[ii] = (jj, current_gas)
                    break



        return -1


    # def ___():


    #     for ii in reversed(range(n)):
    #         init gas

    #         while:
    #             if current_gas >= current_cost:
    #                 if next_posisiton in memo:
    #                     start calculation from position
    #                     assign jj
    #                 else:
    #                     jj++

    #             else:
    #                 store result

    #         if ii == jj:
    #             return ii


if __name__ == "__main__":

    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    gas = [1, 1, 1]
    cost = [3, 3, 3]

    gas = [3,1,1]
    cost = [1,2,2]

    sol = Solution()
    print(sol.canCompleteCircuit(gas, cost))
