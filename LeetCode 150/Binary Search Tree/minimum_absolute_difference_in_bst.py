# 530. Minimum Absolute Difference in BST - easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int: # O(n) time, O(h) space
        '''
            Use the properties of a BST. 
            Do a DFS in-order traversal: left -> root -> right
              - the min difference will always be between two consecutive nodes in an in-order traversal
        '''
        stack = []

        curr = root
        prev = None

        min_diff = float('inf')

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()

            if prev is not None:
                min_diff = min(min_diff, curr.val - prev)
            
            prev = curr.val
            curr = curr.right
    
        return min_diff
