class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store numbers and their indices
        memory = {}

        # Iterate through nums
        for pos, num in enumerate(nums):
            # Calculate the complement
            target_num = target - num

            # Check if the complement is in memory
            if target_num in memory:
                return [memory[target_num], pos]

            # Store the current number and its index
            memory[num] = pos

        return []