class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        source = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        specials = {
            "IV": "IIII",
            "IX": "VIIII",
            "XL": "XXXX",
            "XC": "LXXXX",
            "CD": "CCCC",
            "CM": "DCCCC"
        }

        for spe in specials:
            s = s.replace(spe, specials[spe])
        for i in s:
            result += source[i]

        return (result)
