from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k: int = 1

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
