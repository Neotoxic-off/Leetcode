import re

class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub(' +', ' ', s)

        return " ".join(s.strip().split(' ')[::-1])
