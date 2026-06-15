# 230. Kth Smallest Element in a BST - medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            Given the root of a BST, return the kth smallest value
            Important: tree is 1-indexed

            Since we are given a BST, this means that duplicates aren't allowed and we could also do an inorder traversal to get the tree in ascending order. Since this tree is 1-indexed, we can just return the element at k-1.
        '''
        def inorder(root, res):
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)

        inorder_res = []
        inorder(root, inorder_res)

        return inorder_res[k-1]

        # O(n) time, O(n) space
