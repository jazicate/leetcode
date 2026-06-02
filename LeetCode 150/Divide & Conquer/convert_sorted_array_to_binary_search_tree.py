# 108. Convert Sorted Array to Binary Search Tree - easy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]: # O(n) time, O(n) space
        '''
            Given int array nums
              - the elements are sorted in ascending order
            Convert it to a height-balanced BST.

            A straight forward solution would just be to build a BST by inserting elements one by one then balancing it out afterwards. This solution does take O(n^2) time.

            A more optimal solution would be a divide and conquer approach. Since the array is already sorted, that means that we could choose the middle element as the root of the BST to keep the tree balanced. So everything to the left of the middle element is smaller than the root, so they can be used to build the left subtree and same idea for the right elements to build the right subtree. We recursively do this until there are no elements left.
        '''
        def buildBST(left, right):
            if left > right:
                return None
            
            mid = (left+right) // 2
            new_node = TreeNode(nums[mid])

            new_node.left = buildBST(left, mid-1) # exclude mid
            new_node.right = buildBST(mid+1, right) # exclude mid

            return new_node

        return buildBST(0, len(nums)-1)
'''
Time Complexity:
T(n) = 2T(n/2) + O(1)

T(n) = 2[2T(n/4) + 1] + 1
T(n) = 4T(n/4) + 2 + 1
T(n) = 8T(n/8) + 4 + 2 + 1

So:
Level 0: 1
Level 1: 2
Level 2: 4
...

1 + 2 + 4 + ... + n = 2n - 1 -> O(n)
T(n) = O(n)

Space Complexity:
aux space + total space

aux space = O(logn) # new_node.left is finished before new_node.right
  - recursion stack has height log n since the tree is height-balanced
total space = O(n)

-> O(n) space
'''