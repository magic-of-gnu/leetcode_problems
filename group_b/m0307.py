class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0] * (len(nums) + 1)

        current_sum = 0
        for ii in range(len(nums)):
            current_sum += nums[ii]
            self.prefix_sum[ii+1] = current_sum

    def update(self, index: int, val: int) -> None:

        num = self.prefix_sum[index+1] - self.prefix_sum[index]
        diff = num - val

        for ii in range(index+1, len(self.prefix_sum)):
            self.prefix_sum[ii] -= diff

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]


class Node:
    def __init__(self, val, left=None, right=None, rleft=None, rright=None):
        self.val = val
        self.left = left
        self.right = right

        self.rleft = rleft
        self.rright = rright


class SegmentTree:
    def __init__(self, nums):
        n = len(nums)

        prefix_sum = [0] * n
        current_sum = 0

        for ii in range(n):
            current_sum += nums[ii]
            prefix_sum[ii] = current_sum

        self.root = Node(prefix_sum[-1], rleft=0, rright=n-1)

        left, right = 0, n-1

        

class NumArray:
    def __init__(self, nums):
        self.segment_tree = [0] * (len(nums) + 1)

        current_sum = 0
        for ii in range(len(nums)):
            current_sum += nums[ii]
            self.prefix_sum[ii+1] = current_sum

    def update(self, index: int, val: int) -> None:

        num = self.prefix_sum[index+1] - self.prefix_sum[index]
        diff = num - val

        for ii in range(index+1, len(self.prefix_sum)):
            self.prefix_sum[ii] -= diff

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)



if __name__ == "__main__":

    nums = [1, 3, 5]
    commands =  [0, 2], [1, 2], [0, 2]

    sol = NumArray(nums)
    print(sol.sumRange(*commands[0]))
    print(sol.update(*commands[1]))
    print(sol.sumRange(*commands[2]))
