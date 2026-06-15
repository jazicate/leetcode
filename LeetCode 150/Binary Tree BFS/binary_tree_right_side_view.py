# 199. Binary Tree Right Side View - medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
            Given root of a binary tree, return the nodes that you can see from the right side from top to bottom.

            A BFS is perfect for this because we can get the last node of each level.
        '''
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()

                # If the node is the last node at this level
                if _ == size-1: 
                    res.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return res

    # O(n) time, O(n) space