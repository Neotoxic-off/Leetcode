class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        max_size = len(min(strs, key=len))
        result = ""

        for _str in strs:
            for i in range(max_size):
                result = _str[:max_size - i]
                if (self.__all_starts__(result, strs) == True):
                    return (result)

        return ("")

    def __all_starts__(self, word, strs):
        for s in strs:
            if (s.startswith(word) == False):
                return (False)
        return (True)
