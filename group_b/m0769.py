# 769. Max Chunks To Make Sorted

# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.
# 
# What is the most number of chunks we could have made?


# 05 June 2021


class Solution:
    def maxChunksToSorted(self, arr):

        def is_consecutive(seen, min_value, max_value):
            # return (max_value - min_value + 1) == len([x for x in seen.keys() if x >= min_value and x <= max_value])
            return (max_value - min_value + 1) == len([x for x in seen if x >= min_value and x <= max_value])

        min_value = 0
        # seen = dict()
        seen = set()
        num_chunks = 0


        for ind, x in enumerate(arr):
            # seen[x] = 1
            seen.add(x)

            if is_consecutive(seen, min_value, ind):
                num_chunks += 1
                seen = set()
                min_value = ind + 1

        return num_chunks

class Solution:
    def maxChunksToSorted(self, arr):

        def is_consecutive(seen, min_value, max_value):
            # return (max_value - min_value + 1) == len([x for x in seen.keys() if x >= min_value and x <= max_value])
            return (max_value - min_value + 1) == len([x for x in seen if x >= min_value and x <= max_value])

        num_chunks = 0
        cur_max = -1

        for ind, x in enumerate(arr):
            cur_max = max(cur_max, x)

            if max(cur_max, x) == ind:
                num_chunks += 1


        return num_chunks


if __name__ == "__main__":
    # arr = [4,3,2,1,0]
    # Output = 1

    arr = [2,0,1]
    Output = 1

    arr = [1,0,2,3,4]
    Output = 4

    sol = Solution()
    print(sol.maxChunksToSorted(arr))
