# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodNodeFinder(node, maxVal) -> int:
            if not node:
                return 0
            
            res = 0 if maxVal > node.val else 1
            
            left = goodNodeFinder(node.left, max(maxVal, node.val))
            right = goodNodeFinder(node.right, max(maxVal, node.val))

            return res + left + right

        ans = goodNodeFinder(root, root.val)
        
        return ans