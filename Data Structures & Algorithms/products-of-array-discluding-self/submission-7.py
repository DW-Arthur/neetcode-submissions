class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix post fix
        # Somehow make the prefix and postfix array
        # Then at easy index, multiply the prefix and postfix
        # For this prefix and postfix problem, these are exclusive prefix/postfix arrays
        # Where the current element it self is excluded
        # Ex: [1,2,4,6]
        # Prefix exlusive [1,1,2,24]
        # Postfix exlusive[48,24,6,1]
        # Ex: [-1,0,1,2,3]
        # Prefix exclusive [1,-1,0,0,0]
        # Postfix exclusive[0,6,6,3,1]
        # prefix[1] = 1 x nums[0] = nums[0]
        result = []
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix[i] = 1
                continue
            num = prefix[i-1] * nums[i-1]
            prefix[i]= num
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix[i] = 1
                continue
            postfix[i] = postfix[i+1] * nums[i+1]
        for i in range(len(nums)):
            product = prefix[i] * postfix[i]
            result.append(product)
        return result
