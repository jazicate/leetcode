# 101. Symmetric Tree - easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
            Iterative Version: BFS -> O(n) time, O(n) space
        '''
        # queue = deque([(root.left, root.right)])

        # while queue:
        #     tree1, tree2 = queue.popleft()

        #     if not tree1 and not tree2:
        #         continue
        #     if not tree1 or not tree2:
        #         return False
        #     if tree1.val != tree2.val:
        #         return False
            
        #     queue.append((tree1.left, tree2.right))
        #     queue.append((tree1.right, tree2.left))

        # return True
        
        '''
            Recursive Version: DFS -> O(n) time, O(h)/O(n) space
        '''
        def mirror(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            if tree1.val != tree2.val:
                return False

            return mirror(tree1.left, tree2.right) and mirror(tree1.right, tree2.left)
        
        if not root:
            return True

        return mirror(root.left, root.right)
