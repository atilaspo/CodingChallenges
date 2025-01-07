class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different
        if len(s) != len(t):
            return False

        # Create dictionaries to count character frequencies
        mem_s = {}
        mem_t = {}

        # Count characters in s
        for ch in s:
            mem_s[ch] = mem_s.get(ch, 0) + 1

        # Count characters in t
        for ch in t:
            mem_t[ch] = mem_t.get(ch, 0) + 1

        # Compare the dictionaries
        return mem_s == mem_t
