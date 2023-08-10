class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, n in enumerate(nums):
            if n in num_dict:
                return [num_dict[n], i]
            else:
                num_dict[target-n] = i
