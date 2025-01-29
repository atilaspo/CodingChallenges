class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            M = (L + R) // 2
            if nums[M] == target:
                return nums.index(target)
            elif nums[M] > target:
                R = M - 1
            else:
                L = M + 1
        
        return -1