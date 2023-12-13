class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        index = 0
        buffer = []
        word = None

        if (size > 1):
            while (index < size):
                for i in range(index, size):
                    word = s[index:i + 1]
                    if (self.__is_palindrom__(word) == True):
                        buffer.append(word)
                index += 1

            return (max(buffer, key=len))
        return (s)

    def __is_palindrom__(self, data):
        return (data == data[::-1])
