class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        max_left = height[l]
        max_right = height[r]
        water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                max_left = max(max_left, height[l])
                water += max_left - height[l]

            else:
                r -= 1
                max_right = max(max_right, height[r])
                water += max_right - height[r]
        
        return water