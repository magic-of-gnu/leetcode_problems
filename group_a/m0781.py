# 781. Rabbits in Forest

# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

# Given the array answers, return the minimum number of rabbits that could be in the forest.

from collections import Counter


class Solution:
    # def numRabbits(self, answers: List[int]) -> int:
    def numRabbits(self, answers):
        num_rabbits = 0
        counter = Counter(answers)

        for ans, count in counter.items():
            num_rabbits += (count // (ans + 1)) * (ans + 1)

            if count % (ans + 1) != 0:
                num_rabbits += ans + 1

        return num_rabbits


if __name__ == "__main__":
    answers = [1,1,2]
    Output = 5

    answers = [4,4,4,4,4,4]
    Output = 10

    answers = [4,4,4,4,4,4,4]
    Output = 10

    sol = Solution()
    print(sol.numRabbits(answers))
