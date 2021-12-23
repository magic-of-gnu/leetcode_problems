class Solution:
    def maxScore(self, cardPoints, k: int) -> int:

        lsum = [0] * (k+1)
        rsum = [0] * (k+1)

        lcurr_sum = 0
        rcurr_sum = 0

        for ii in range(k):
            lcurr_sum += cardPoints[ii]
            rcurr_sum += cardPoints[-(ii+1)]

            lsum[   ii+1 ] = lcurr_sum
            rsum[ -(ii+2)] = rcurr_sum

        max_score = 0

        for ii in range(k+1):
            max_score = max(max_score, lsum[ii] + rsum[ii])

        return max_score

    def maxScore(self, cardPoints, k):

        sum_window = sum(cardPoints[:k])
        max_score = sum_window

        for ii in range(k):
            sum_window = sum_window - cardPoints[k-1-ii] + cardPoints[-(ii+1)]
            max_score = max(max_score, sum_window)

        return max_score




if __name__ == "__main__":
    cardPoints = [1,79,80,1,1,1,200,1]
    k = 3

    cardPoints = [96,90,41,82,39,74,64,50,30]
    k = 8

    sol = Solution()
    print(sol.maxScore(cardPoints, k))
