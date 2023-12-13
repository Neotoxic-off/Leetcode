class Solution:
    def reverse(self, x: int) -> int:
        s = f"{x}"[::-1]
        n = False
        if (x < 0):
            n = True

        if (s.startswith('0')):
            s = s[self.__extract_f_o__(s, '0'):]
            if (len(s) == 0):
                return (0)
        if (s.endswith('-')):
            s = s[:len(s) - 1]

        if (n == True):
            r = int(s) * -1
        else:
            r = int(s)
        if (r >= pow(-2, 31) and r <= (pow(2, 31) - 1)):
            return (r)
        return (0)
    
    def __extract_f_o__(self, d, c):
        r = 0
        for i in range(len(d)):
            if d[i] != c:
                return (r)
            r += 1
        return (r)
