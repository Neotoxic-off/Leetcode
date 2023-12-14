class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = -1
        r = {}

        for i in nums:
            if (i not in r.keys()):
                r[i] = 0
            r[i] += 1
        for key in r.keys():
            if (m == -1):
                m = key
            if (r[key] > r[m]):
                m = key

        return m
