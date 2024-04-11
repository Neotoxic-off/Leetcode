class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1):
            for j in range(i, len(nums) - 1):
                if (bin(nums[i] | nums[j + 1]).endswith('0') == True):
                    return True
        return False
