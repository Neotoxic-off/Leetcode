class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        def get_bucket(num, width):
            return (num // width)

        bucket_width = valueDiff + 1
        buckets = {}

        for index, num in enumerate(nums):
            bucket = get_bucket(num, bucket_width)
            if bucket in buckets:
                return True
            if (bucket - 1) in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True
            if (bucket + 1) in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True
            buckets[bucket] = num
            if index >= indexDiff:
                del buckets[get_bucket(nums[index - indexDiff], bucket_width)]

        return False
