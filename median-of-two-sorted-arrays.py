class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a = nums1 + nums2

        return (self.median(a))

    def median(self, data):
        data.sort()
        mid = len(data) // 2
        return (data[mid] + data[~mid]) / 2.0
