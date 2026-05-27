# 74. Search a 2D Matrix - med
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: # O(log(mn))
        '''
            Given a m x n in matrix with:
              - each ROW is sorted in non-decreasing order
              - the first int of each ROW is greater than the last int of the previous ROW
            Given an int target
              - Return true if target is in matrix
              - Else return false if not
            Write solution in O(log(mn))

            Interview Prep: 
            So we are essentially searching through a 2D int array to see if a target number or element exists.
            A solution would just be to brute force by iterating through all the elements, but that would be O(nm) and the problem suggests to create it in O(log(mn)).
            A more efficient approach would be to use a binary search since each row is already sorted.
            With this approach, we could also treat the 2d matrix as a single array due to the properties given.
        '''

        m = len(matrix) # rows
        n = len(matrix[0]) # cols

        left, right = 0, m*n-1
        while left <= right:
            mid = (left+right) // 2

            # Convert 1D indices to 2D matrix position
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
