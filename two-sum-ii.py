class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers
        l, r = 0, len(numbers) - 1
        
        while l < r:
            current_sum = numbers[l] + numbers[r]
            
            # Adjust pointers based on the sum
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                # Return 1-indexed result
                return [l + 1, r + 1]
        
        return []