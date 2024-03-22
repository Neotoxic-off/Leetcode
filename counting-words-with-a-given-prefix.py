class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0

        for word in words:
            if word.startswith(pref) == True:
                count += 1
        
        return count
