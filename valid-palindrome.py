class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Get all the characters that are alphanumeric and convert to lowercase
        s = ''.join(ch for ch in s if ch.isalnum()).lower()

        # Create two pointers
        i = 0
        j = len(s) - 1  # j points to the last character
        
        # Check characters from both ends
        while i < j:
            if s[i] != s[j]:
                return False
            # Move pointers inward
            i += 1
            j -= 1
        
        return True