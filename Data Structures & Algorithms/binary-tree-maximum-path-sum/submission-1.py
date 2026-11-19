# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxVal = root.val

        def dfs(node) -> int:
            if not node:
                return 0 

            max_left = dfs(node.left)
            max_right = dfs(node.right)

            sum_through_node = node.val + max_left + max_right
            self.maxVal = max(self.maxVal, sum_through_node)

            return node.val + max(max_left, max_right)

        dfs(root)
        return self.maxVal