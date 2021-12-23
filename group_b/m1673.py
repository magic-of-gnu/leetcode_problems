class Solution:
    # def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
    def mostCompetitive(self, nums, k):

        n = len(nums)
        st = []

        for ii, val in enumerate(nums):
            while True:
                if not st:
                    break

                if len(st) + n - ii <= k:
                    break

                if st[-1] <= val:
                    break
                    
                st.pop()

            if len(st) < k:
                st.append(val)

        return st


if __name__ == "__main__":
    nums = [3,5,2,6]
    k = 3

    nums = [2,4,3,3,5,4,9,6,6,6,6,6]
    k = 4

    sol = Solution()
    print(sol.mostCompetitive(nums, k))
