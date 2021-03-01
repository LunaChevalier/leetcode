#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 1, 1
        while j < len(nums):
            if not nums[i - 1] == nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
            print(nums)
        return i
# @lc code=end
