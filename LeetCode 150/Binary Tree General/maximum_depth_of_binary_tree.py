# 104. Maximum Depth of Binary Tree - Easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: # O(n) time, O(h) space
        '''
            Post-order DFS
            Get height of left subtree
            Get height of right subtree

            return the higher subtree + 1 (current node)
        '''
        if not root:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        return 1 + max(left_height, right_height)
