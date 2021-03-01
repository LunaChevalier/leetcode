#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        rep_s = s
        while True:
            tmp = rep_s
            rep_s = rep_s.replace("()", "")
            rep_s = rep_s.replace("[]", "")
            rep_s = rep_s.replace("{}", "")
            if tmp == rep_s: break
        return False if rep_s else True
# @lc code=end

