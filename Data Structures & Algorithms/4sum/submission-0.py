class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 3 pointers in this case?
        # No 1 for loops, and only then there are 2 pointers, left and right
        # What are edget cases
        # Since the theres must be distinct, i cant have repeat characters per loop
        # For the i and j, I need to check that if i -1 is the the same
        result =[]
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j +1
                right = len(nums)-1
                while left < right:
                    total = nums[left] + nums[right] + nums[i] + nums[j]
                    if total < target:
                        left +=1
                    elif total > target:
                        right -=1
                    elif total == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left +=1
                        right -=1
                        while left < right and nums[left] == nums[left-1]:
                            left +=1
                        while left < right and nums[right] == nums[right+1]:
                            right -=1
        return result

        