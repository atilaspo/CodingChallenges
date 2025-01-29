class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        # Step 1: Binary search to find the correct row
        TOP = 0
        BOTTOM = ROWS - 1
       
        while TOP <= BOTTOM:
            MED = (TOP + BOTTOM) // 2
            if target < matrix[MED][0]:  # Target is smaller than first element in the row
                BOTTOM = MED - 1
            elif target > matrix[MED][-1]:  # Target is greater than the last element in the row
                TOP = MED + 1
            else:
                break  # Found the row that may contain the target
        
        # If target is out of matrix bounds
        if not (TOP <= BOTTOM):
            return False

        # Step 2: Binary search within the identified row
        MED = (TOP + BOTTOM) // 2
        L = 0
        R = COLS - 1

        while L <= R:
            M = (L + R) // 2
            if matrix[MED][M] > target:  # Move left
                R = M - 1
            elif matrix[MED][M] < target:  # Move right
                L = M + 1
            else:
                return True  # Target found
        
        return False  # Target not found in the matrix
