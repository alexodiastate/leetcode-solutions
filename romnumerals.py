class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        numerals = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }

        out = 0
        for i in range(len(s)):
            curr = numerals[s[i]]
            if i + 1 < len(s) and curr < numerals[s[i+1]]:
                out -= numerals[s[i]]
            else:
                out += numerals[s[i:i+1]]
        return out