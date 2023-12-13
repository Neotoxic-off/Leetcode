class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        for i in range(l):
            if (nums[i] >= target):
                return i
        return (l)
