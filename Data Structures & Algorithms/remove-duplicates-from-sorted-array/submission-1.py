class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two pointers, left and right
        # Since the array is sorted, have the left pointer be at the index where the next
        # unique element is placed
        # Right pointer keeps going searching for unique element
        write,read = 1,1
        while read < len(nums):
            if nums[read] != nums[read-1]:
                nums[write] =nums[read]
                write +=1
            read+=1
        return write
