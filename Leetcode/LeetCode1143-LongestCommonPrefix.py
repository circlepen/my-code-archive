"""
Question:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

"""

import enum


class Solution:
    def longest_common_prefix(self, strs: 'List[str]') -> 'str':
        if not strs:
            return ""
        # min, max 用首字母的順序來排序
        s1 = min(strs)
        s2 = max(strs)
        print(s1, s2)
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1


if __name__ == '__main__':
    s = Solution()
    ans = s.longest_common_prefix(["flower", "flow", "flight"])
    print(ans)

    ans = s.longest_common_prefix(["aoge", "racecar", "rac"])
    print(ans)
