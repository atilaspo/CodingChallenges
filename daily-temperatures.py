class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a stack to track temperatures and their indices
        stack = []
        # Initialize result array with 0s
        res = [0] * len(temperatures)

        # Iterate through temperatures with their indices
        for i, temp in enumerate(temperatures):
            # While the current temperature is warmer than the last in the stack
            while stack and temp > stack[-1][0]:
                stack_temp, stack_i = stack.pop()  # Pop the last temperature and index
                res[stack_i] = i - stack_i  # Update the result for the index
            # Push the current temperature and its index onto the stack
            stack.append([temp, i])

        return res