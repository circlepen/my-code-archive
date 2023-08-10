"""
Question:
Given an array nums of n integers, are there elements a, b, c in numssuch 
that a + b + c = 0? Find all unique triplets in the array which 
gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        ans = []
        for i, v in enumerate(nums[:-2]):
            # 如果這個數字跟前一個一樣就跳過，不然會有重複答案
            if i >= 1 and v == nums[i-1]:
                continue
            numMaps = {}
            for j in nums[i+1:]:
                if j in numMaps.keys():
                    new_ans = (v, numMaps[j], j)
                    ans.append(new_ans)
                else:
                    numMaps[-v-j] = j

        return ans


if __name__ == "__main__":
    s = Solution()
    ans = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(ans)
