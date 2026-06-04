# 637. Average of Levels in Binary Tree - easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''
            DFS version - O(n) time, O(n) space
        '''
        # res = []

        # elements = []
        # def preOrder(root, level, elements):
        #     if not root:
        #         return

        #     if len(elements) <= level:
        #         elements.append([])
            
        #     elements[level].append(root.val)

        #     preOrder(root.left, level+1, elements)
        #     preOrder(root.right, level+1, elements)

        # preOrder(root, 0, elements)
        # print(elements) # elements should be put into level-order

        # for it in elements:
        #     if it:
        #         res.append(sum(it)/len(it))

        # return res

        '''
            BFS version - O(n) time, O(n) space
        '''
        res = []

        queue = deque([root])
        while queue:
            level_total = 0
            level_nodes = len(queue)

            for _ in range(level_nodes):
                curr = queue.popleft()

                level_total += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            res.append(level_total/level_nodes)
            
        return res
        