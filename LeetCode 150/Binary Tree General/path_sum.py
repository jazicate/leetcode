# 112. Path Sum - easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
            Approach:
            Do a DFS to check every path from root to leaf while keeping track of a current sum of the node values. When a leaf is reached, check if the current sum is equal to the target sum.
        '''
        def dfs(node, currentSum):
            if not node:
                return False

            currentSum += node.val

            if not node.left and not node.right:
                return currentSum == targetSum

            return dfs(node.left, currentSum) or dfs(node.right, currentSum)
        
        return dfs(root, 0)

        # O(n) time, O(h) space where h is the height of the tree
