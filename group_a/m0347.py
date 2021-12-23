# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from collections import defaultdict

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        counter = defaultdict(int)

        max_count = 0

        for x in nums:
            counter[x] += 1
            max_count = max(max_count, counter[x])


        freq = defaultdict(list)
        [freq[count].append(letter) for letter, count in counter.items()]

        result = []
        freq_keys = reversed(sorted(freq.keys()))

        while True:
            result += freq[next(freq_keys)][:k-len(result)]
            if len(result) >= k:
                return result[:k]


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]; k = 2
    Output = [1,2]

    nums = [1,2]; k = 2
    Output = [1, 2]


    sol = Solution()
    print(sol.topKFrequent(nums, k))
