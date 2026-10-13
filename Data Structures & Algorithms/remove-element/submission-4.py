class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1 and nums[0] == val:
            return 0
        i, right = 0 , len(nums)-1
        k=0
        while i <=right:
            if nums[i] == val:
                nums[i] = nums[right]
                nums[right] = val
                right -=1
                k+=1
            else:
                i+=1
        return len(nums)-k

        