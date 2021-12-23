
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums):

        num2gr = dict()
        gr2count = defaultdict(int)
        gr2gr = defaultdict(set)
        count = 0

        for x in nums:

            if x in num2gr:
                continue

            pgr = num2gr.get(x-1)
            ngr = num2gr.get(x+1)

            gr = num2gr.get(x-1, num2gr.get(x+1, count))
            if gr == count:
                count += 1

            num2gr[x] = gr
            gr2count[gr] += 1

            if ngr is not None and pgr is not None:
                gr2gr[ngr].add(pgr)
                gr2gr[pgr].add(ngr)

        def traverse(gr2gr, gr, current_path, seen):
            if gr in seen:
                return

            current_path.add(gr)
            seen.add(gr)

            for child in gr2gr.get(gr, set()):
                traverse(gr2gr, child, current_path, seen)

            return

        result = 0
        seen = set()

        for x in range(count):
            current_path = set()
            c = 0
            traverse(gr2gr, x, current_path, seen)

            for gr in current_path:
                c += gr2count[gr]

            result = max(result, c)

        return result



if __name__ == "__main__":
    nums = [0,5,3,7,1,4,6,2,10,44,45,50,60,51,59,55,58,57,54,52,55,53,56,61]

    sol = Solution()
    print(sol.longestConsecutive(nums))
