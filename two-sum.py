class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if (nums[i] + nums[j] == target and i != j):
                    result = ([i, j])
        return (result)
