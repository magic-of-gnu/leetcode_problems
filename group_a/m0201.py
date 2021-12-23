class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        def get_dist_till_flip(num, ii):
            s = 1 << ii
            return s - num % (s)

        result = 0
        for ii in range(32):
            dist_till_flip = get_dist_till_flip(left, ii)
            result = result | (((left>>ii & 1) & (dist_till_flip > (right-left))) << ii)

        return result 
