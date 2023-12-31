"""
Question:
Given a sorted nums array, remove the duplicates in-place such that each element 
appears only once and return the new length.
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            print("nums looks like: ", nums)
            return 0

        prev = nums[0]
        count = 1
        for v in nums[1:]:
            if prev != v:
                nums[count] = v
                prev = v
                count += 1

        print("nums looks like: ", nums)
        return count


if __name__ == "__main__":
    s = Solution()
    ans = s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(ans)
    ans = s.removeDuplicates([1, 1, 2])
    print(ans)
    ans = s.removeDuplicates([])
    print(ans)
    ans = s.removeDuplicates([3])
    print(ans)
