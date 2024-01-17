class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        data = {}

        for element in arr:
            if element in data.keys():
                data[element] += 1
            else:
                data[element] = 0

        for v in data.values():
            if list(data.values()).count(v) > 1:
                return (False)
        return (True)
