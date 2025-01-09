class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, val in enumerate(nums):
            if i > 0 and nums[i -1] == val:
                continue
            
            
            l = i + 1
            r = len(nums) -1
            
            while l < r:
                current_sum = val + nums[l] + nums[r]

                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result