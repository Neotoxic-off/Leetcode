class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        weight = [
            {},
            {}
        ]

        if (len(s) == len(t)):
            for c in s:
                if (c not in weight[0].keys()):
                    weight[0][c] = s.count(c)
            for c in t:
                if (c not in weight[1].keys()):
                    weight[1][c] = t.count(c)
            return (weight[0] == weight[1])
        return False
