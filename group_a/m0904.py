from collections import defaultdict

class Solution:
    def totalFruit(self, fruits):

        left, right = 0, 0
        basket = defaultdict(int)
        max_count = 0
        k = 2
        n = len(fruits)

        while left <= right and right < n: # 2,6; 1
            # print()
            # print(f'left: {left} right: {right}')
            # print(f'basket: {basket}')
            # print(f'max_count: {max_count}')

            basket[fruits[right]] += 1  # {1:3, 4:2}
            right += 1                  # 7

            # print(f'right: {right}; basket: {basket}')

            while len(basket) > k:
                basket[fruits[left]] -= 1  # 1:1; 0:0, 4:1
                if basket[fruits[left]] == 0: # true
                    basket.pop(fruits[left])  # {1:1, 4:1}

                left += 1                  # 2

                # print(f'basket: {basket}')
                # print(f'left: {left}')

            max_count = max(max_count, right-left) # 4 vs 7-2; 4 vs 5 -> 5

        return max_count



if __name__ == "__main__":
             #0 1 2 3 4 5 6 7 8 9 0 1 2 3
    fruits = [3,3,3,1,2,1,1,2,3,3,2,3,3,4]
            # 0 1 2 3 4 5 6 7 8
    fruits = [1,0,1,4,1,4,1,2,3]
    output = 5

    sol = Solution()
    print(sol.totalFruit(fruits))

