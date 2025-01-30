class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            MED = (L + R) // 2
            if nums[MED] > nums[R]:
                L = MED + 1
            else:
                R = MED
        
        return nums[L]
