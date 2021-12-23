# 1276. Number of Burgers with No Waste of Ingredients

# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:
# 
#     Jumbo Burger: 4 tomato slices and 1 cheese slice.
#     Small Burger: 2 Tomato slices and 1 cheese slice.
# 
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

import math

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo = (tomatoSlices - 2 * cheeseSlices) / 2
        small = cheeseSlices - jumbo
        
        if jumbo < 0 or math.floor(jumbo) != jumbo:
            return []
        if small < 0 or math.floor(small) != small:
            return []
        return [int(jumbo), int(small)]
