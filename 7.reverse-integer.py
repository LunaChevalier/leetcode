#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) > 2 ** 31:
            return 0

        x_str = str(x).replace('-', '')
        x_str = x_str[::-1]

        if int(x_str) > 2 ** 31:
            return 0

        return int(x_str) if x > 0 else int(x_str) * - 1
# @lc code=end
