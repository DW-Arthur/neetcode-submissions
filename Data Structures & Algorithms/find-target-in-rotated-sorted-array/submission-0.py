class Solution:

  def search(self, nums: List[int], target: int) -> int:
    # 1. Find the inflection / minimum element index
    left, right = 0, len(nums) - 1
    while left < right:
      mid = (left + right) // 2
      if nums[mid] > nums[right]:
        left = mid + 1
      else:
        right = mid

    pivot = left  # This is the index of the minimum element

    # 2. Determine which sorted subarray to search
    # nums[pivot..end] is sorted, and nums[0..pivot-1] is sorted
    if pivot == 0:
      left, right = 0, len(nums) - 1
    elif target >= nums[pivot] and target <= nums[-1]:
      left, right = pivot, len(nums) - 1
    else:
      left, right = 0, pivot - 1

    # 3. Standard binary search on the chosen range [left, right]
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      elif nums[mid] < target:
        left = mid + 1
      else:
        right = mid - 1

    return -1