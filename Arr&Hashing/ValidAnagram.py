class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        CountS, CountT = {}, {}
        
        # Populate Dictionaries
        for i in range(len(s)):
            CountS[s[i]] = 1 + CountS.get(s[i], 0)
            CountT[t[i]] = 1 + CountT.get(t[i], 0)
        
        # Check if Populated Dictionaries Match

        for char in CountS:
            if CountS[char] != CountT.get(char, 0):
                return False
        
        return True