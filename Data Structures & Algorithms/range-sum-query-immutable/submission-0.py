class NumArray:

    def __init__(self, nums: List[int]):
        # Initialize the prefix array
        self.prefix = []
        curr = 0
        for i in nums:
            curr += i
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        # All the sum up to right
        r = self.prefix[right]
        # The answer should be the everything sum to the right - everything sum just before
        # the left
        if left -1 <0:
            l = 0
        else:
            l = self.prefix[left-1]
        result = r-l
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)