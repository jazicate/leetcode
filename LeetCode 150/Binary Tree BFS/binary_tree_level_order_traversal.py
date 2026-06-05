# 102. Binary Tree Level Order Traversal - medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            DFS preorder traversal -> LevelOrder output
            O(n) time, O(n) space
        '''
        # def levelOrderHelper(root, level, res):
        #     if not root:
        #         return

        #     if len(res) <= level:
        #         res.append([])
            
        #     res[level].append(root.val)
        #     levelOrderHelper(root.left, level+1, res)
        #     levelOrderHelper(root.right, level+1, res)

        # res = []
        # levelOrderHelper(root, 0, res)
        # return res

        '''
            BFS level order traversal
            O(n) time, O(n) space
        '''
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.append(level)
        
        return res
        