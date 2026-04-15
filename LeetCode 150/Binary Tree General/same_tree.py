# 100. Same Tree - easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: # O(n) time, O(h) space
        '''
            Recursively check each node -> Recursive DFS

            Check if both nodes are None
              - this means they are both None, so they are the same -> return true
            Check if either nodes are None
              - this means they are not the same, therefore return False
            Check if values are the same for both nodes
            Recursively call on the left node and right nodes
        '''
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
