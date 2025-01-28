class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Store characters in the current window
        start = 0  # Start pointer of the window
        max_length = 0  # Maximum length of substring without duplicates

        for end in range(len(s)):
            # If the character is already in the window, shrink the window
            while s[end] in char_set:
                char_set.remove(s[start])  # Remove the leftmost character
                start += 1  # Move the start pointer to the right
            
            # Add the new character to the window
            char_set.add(s[end])
            
            # Update the max length of the substring
            max_length = max(max_length, end - start + 1)
        
        return max_length