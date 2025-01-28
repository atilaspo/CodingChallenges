class Solution:
      def characterReplacement(self, s: str, k: int) -> int:
          # Create a dictionary to store character frequencies in the current window
          memory = {}
          # Left pointer of the sliding window
          L = 0
          # Variable to store the maximum length of the substring
          res = 0

          # Apply sliding window technique
          for R in range(len(s)):
              # Add the current character to the frequency dictionary
              memory[s[R]] = 1 + memory.get(s[R], 0)

              # Check if the current window is invalid
              while (R - L + 1) - max(memory.values()) > k:
                  # Shrink the window by reducing the frequency of the left character
                  memory[s[L]] -= 1
                  L += 1

              # Update the maximum result length
              res = max(res, R - L + 1)

          # Return the length of the longest valid substring
          return res