class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Process string
        final = ""

        for char in s:
            if char.isalnum():
                final += char
        final = final.lower()
        i, j = 0, len(final) - 1

        while i < j:
            if final[i] != final[j]:
                return False
            i += 1
            j -= 1
        
        return True

