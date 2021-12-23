# 1481. Least Number of Unique Integers after K Removals

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# 10 June 2021

from collections import Counter
from collections import defaultdict

class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):

        counter = Counter(arr)

        freqs = defaultdict(list)
        [freqs[value].append(key) for key, value in counter.items()]

        # import pdb; pdb.set_trace()

        val = 1
        current_value = None

        while True:
            if k == 0:
                break

            if current_value is not None:
                k_to_remove = min(k, counter.get(current_value))
                k -= k_to_remove
                counter[current_value] -= k_to_remove
                if counter[current_value] == 0:
                    counter.pop(current_value)
                    current_value = None
                continue

            if len(freqs.get(val, [])) == 0:
                val += 1
                continue

            current_value = freqs.get(val).pop()

        return len(counter.keys())



if __name__ == "__main__":
    arr = [4,3,1,1,3,3,2]; k = 3
    Output = 2

    arr = [5,5,4];
    k = 1
    Output = 1

    arr = [1,2,2,2,2]; k = 4 
    Output = 4

    sol = Solution()
    print(sol.findLeastNumOfUniqueInts(arr, k))
