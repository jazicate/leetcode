# 103. Binary Tree Zigzag Level Order Traversal - medium
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            Given a root of a binary tree
            Return the zigzag level order traversal

            So basically, for each odd number level, we need to reverse its order.

            We initialize a count variable to track the level we are at. Of course, we do a standard level order traversal and after we process each level, we need to check if we are at an odd level. If so, we reverse that level. Finally, at each iteration, we update the level count for the next iteration.
        '''
        if not root:
            return []

        res = []
        queue = deque([root])
        level_count = 0
        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                curr = queue.popleft()
                level.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if level_count % 2 == 1:
                level = level[::-1]
            
            res.append(level)

            level_count += 1
        
        return res

    # O(n) time, O(n) space