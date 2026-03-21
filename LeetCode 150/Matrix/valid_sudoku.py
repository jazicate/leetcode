## 36. Valid Sudoku - Medium
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: # O(81) -> O(1) time, O(1) space
        '''
           - Just checking if the sudoku is valid
           - Need to track the row, column, and each 3x3 sub-box
                - if any of these digits repeat, the board is invalid

            - Technique: We can use a sets first, but a more optimized technique is bit masking.
                - We use bitmasks to track what numbers we have already seen
                    - each row, col, and box is represented by a 9-bit integer
                        - where each digit is mapped to a bit 1 less (digit '1' -> bit 0)
        '''
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                # Map 1 - 9 to 0 - 8
                num = int(val)-1
                mask = 1 << num

                box = (i//3) * 3 + (j//3)

                # Check if bit is already set
                if (rows[i] & mask) or (cols[j] & mask) or (boxes[box] & mask):
                    return False

                # Set bits
                rows[i] |= mask
                cols[j] |= mask
                boxes[box] |= mask

        return True
        