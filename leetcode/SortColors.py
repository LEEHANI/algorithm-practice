# O(n), O(3), in place, counting sort
# O(n^2), O(1), in place
class Solution(object):
    def sortColors(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                continue
            for j in range(i, 0, -1):
                if nums[j-1] <= nums[j]:
                    break
                nums[j-1], nums[j] = nums[j], nums[j-1]
        