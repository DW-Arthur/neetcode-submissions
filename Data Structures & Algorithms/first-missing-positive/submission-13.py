class Solution:

  def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)

    # 1. Cleanse out-of-range numbers (< 1 or > n)
    # Replace them with n + 1 so they don't interfere with signs
    for i in range(n):
      if nums[i] <= 0 or nums[i] > n:
        nums[i] = n + 1

    # 2. Use values as indices and mark target index negative
    for i in range(n):
      val = abs(nums[i])
      if val <= n:
        idx = val - 1
        # Use abs() to ensure it turns negative even if already negative
        nums[idx] = -abs(nums[idx])

    # 3. First cell that remains positive tells us the missing integer
    for i in range(n):
      if nums[i] > 0:
        return i + 1

    # 4. If all 1..n were found, the answer is n + 1
    return n + 1