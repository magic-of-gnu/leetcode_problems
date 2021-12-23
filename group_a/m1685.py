# 1685. Sum of Absolute Differences in a Sorted Array

class Solution:
    # def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    def getSumAbsoluteDifferences(self, nums):

        count_neg, count_pos = 0, 0
        count_zeros = 0
        bf_neg, bf_neg_count = 0, 0
        bf_pos, bf_pos_count = 0, 0
        sum_neg, sum_pos = 0, 0
        result = []

        for x in nums:
            if x < 0:
                count_neg += 1
                sum_neg += abs(x)
            elif x > 0:
                count_pos += 1
                sum_pos += x

        print(f'sum_neg: {sum_neg}')
        print(f'sum_pos: {sum_pos}')
        print(f'count_neg: {count_neg} count_pos: {count_pos}')

        for x in nums:
            if x < 0:
                x = abs(x)
                r = abs(bf_neg - x * bf_neg_count) + \
                        abs(sum_neg - bf_neg - x * (count_neg - bf_neg_count)) + \
                        x * count_zeros + sum_pos + count_pos * x

                bf_neg += abs(x)
                bf_neg_count += 1
            elif x == 0:
                r = sum_neg + sum_pos
            elif x > 0:
                r = sum_neg + abs(count_neg * x) + \
                       abs(x * count_zeros) + \
                       abs(bf_pos - x * bf_pos_count) + \
                       abs(sum_pos - bf_pos - x * (count_pos - bf_pos_count))
                bf_pos += abs(x)
                bf_pos_count += 1

            result.append(r)

        return result


if __name__ == "__main__":
    nums = [-2,-1,1,2,5]
    nums = [3,4,5,6]

    sol = Solution()
    print(sol.getSumAbsoluteDifferences(nums))
