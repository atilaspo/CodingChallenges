class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        window_size = len(s1)
        window_s2_ch_count = [0] * 26
        s1_ch_count = [0] * 26

        for ch in s1:
            s1_ch_count[ord(ch) - ord('a')] +=1

        for i in range(window_size):
            window_s2_ch_count[ord(s2[i]) - ord('a')] +=1

        if s1_ch_count == window_s2_ch_count:
            return True
        
        for i in range(window_size, len(s2)):
            window_s2_ch_count[ord(s2[i]) - ord('a')] += 1
            window_s2_ch_count[ord(s2[i - window_size]) - ord('a')] -= 1

            if s1_ch_count == window_s2_ch_count:
                return True
        return False