class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Turn the array into a linked list
        # Index points the value of the nums
        # Index --> nums[i]
        # Think of of the current index as the room you are staying ing
        # Think about the value of the index you are pointng to next
        # [1,2,3,2,2]
        # Room 0, points to room 1
        # Room 1, points to room 2
        # Room 2, poionts to room 3
        # Room 3, points to room 2
        # Room 4, points to room 2 
        # [1, 3, 4, 2, 2]
        # Room 0, points to room 1
        # Room 1, points to room 3
        # Room 2, points to room 4
        # Room 3, points to room 2
        # Room 4, points to room 2
        # List all the indices as nodes !important
        # Then connect their values later
        # Phase 1: Detect cycle and find intersection
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]  # Fixed: must be fast, not slow!

        # Phase 2: Reset one pointer to the start (Index 0)
        fast = 0
        while slow != fast:
            slow = nums[slow]  # speed 1
            fast = nums[fast]  # speed 1

        return slow