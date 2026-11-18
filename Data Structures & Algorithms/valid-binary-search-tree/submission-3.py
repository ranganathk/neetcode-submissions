# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validTree(node, lowerBound, upperBound) -> bool:
            if not node:
                return True
            
            if not (node.val > lowerBound and node.val < upperBound):
                return False 

            left = validTree(node.left, lowerBound, node.val)
            right = validTree(node.right, node.val, upperBound)

            return left and right
        
        ans = validTree(root, -math.inf, math.inf)

        return ans
            
            