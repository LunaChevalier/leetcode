#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        if len(set(strs)) == 1:
            return strs[0]

        max_length = max(map(len, strs))
        for i in range(max_length):
            if len(set(str[0:(i + 1)] for str in strs)) > 1:
                return set(str[0:i] for str in strs).pop()

        return ""

# @lc code=end

