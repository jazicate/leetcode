# 105. Construct Binary Tree from Preorder and Inorder Traversal - medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
            Given two int arrays: 
              - preorder for preorder traversal of tree
              - inorder for inorder traversal of tree
            Construct the original binary tree from these arrays

            Constraints:
              - preorder and inorder consist of UNIQUE values

            Preorder: N > L > R
            Inorder: L > N > R

                3
               / \
              9   20
                  / \
                 15  7

            preorder = [3, 9, 20, 15, 7]
            inorder = [9, 3, 15, 20, 7]

            Observations: 
              - First element in preorder is the root node
              - For inorder, we know everything from the left of the root is going to be in the left subtree, and everything on the right is going to be in the right subtree
                - We also need to find the root node index in inorder -> O(n)
                - We also get the size of the left sub tree
                  -  With this size of the left sub tree, we know this amount of size nodes in preorder go to the left sub tree
                  - The remaining nodes go to the right sub tree

              - We can recursively apply this idea to the left and right subtrees
            
            > So pretty much preorder tells the root, while inorder tells where to split left and right subtrees.
        '''
        # preorder_index = 0

        # def build(left, right):
        #     nonlocal preorder_index

        #     if left > right:
        #         return None

        #     root_val = preorder[preorder_index]
        #     root = TreeNode(root_val)
            
        #     preorder_index += 1

        #     # Find root in inorder
        #     mid = left
        #     while inorder[mid] != root_val:
        #         mid += 1

        #     root.left = build(left, mid-1) # Everything left of mid is in the left subtree
        #     root.right = build(mid+1, right) # Everything right of mid is in the right subtree

        #     return root
        
        # return build(0, len(preorder)-1)
        # O(n^2) time , O(n) space 

        # ------------------------------------------------------------------------
        # NeetCode Solution
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])

        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root
        # O(n^2) time, O(n^2) space

        # ------------------------------------------------------------------------
        # Optimized Solution -> hashmap
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_val = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val] # Find root position in inorder in O(1)

            root.left = build(left, mid-1)
            root.right = build(mid+1, right)

            return root
        
        return build(0, len(inorder) - 1)

        # O(n) time, O(n) space
