class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = []
        max_len = 0
        for char in s:
            if char not in ans:
                ans.append(char)
            else:
                max_len = max(len(ans), max_len)
                idx = ans.index(char)
                if ans[idx] == ans[-1]:
                    ans = [char]
                else:
                    ans = ans[idx+1:] + [char]
        return max(len(ans), max_len)
