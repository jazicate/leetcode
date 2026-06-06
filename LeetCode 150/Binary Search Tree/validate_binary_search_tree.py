# 98. Validate Binary Search Tree - medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        '''
            Pretty much checking if the left subtree is less than the root node and right subtree is greater than the root node, but also need to check ancestors as well. 

            Approach: 
            Do a DFS with bounds: min and max values to keep track of the smallest or largest value the node is allowed to be greater than or less than
              - For the left child, update the upper bound to the current node's value
              - For the right child, update the lower bound to the current node's value

            O(n) time 
            O(h) space, O(logn) if balanced tree and O(n) if skewed
        '''
        def helper(min_value, root,  max_value):
            if not root:
                return True
            
            if not (min_value < root.val < max_value):
                return False

            return helper(min_value, root.left, root.val) and \
                   helper(root.val, root.right, max_value)
        
        return helper(-inf, root, inf)

'''
    20
   /  \
  10  30
      /
     15

  helper(-inf, 20, inf):
    -inf < 20 < inf -> good
    helper(-inf, 10, 20) and helper(20, 30, inf)

    helper(-inf, 10, 20):
      -inf < 10 < 20 -> good -> True
    helper(20, 30, inf):
      20 < 30 < inf -> good -> True
      helper(20 < 15 < 30) -> bad -> False
'''