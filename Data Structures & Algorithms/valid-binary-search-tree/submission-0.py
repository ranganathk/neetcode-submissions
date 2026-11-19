# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validTree(node, parentVal, isLeft) -> bool:
            if not node:
                return True
            
            res = False

            if isLeft:
                if (node.val < parentVal):
                    res = True
                else:
                    res = False
            else:
                if (node.val > parentVal):
                    res = True
                else:
                    res = False
                
            left = validTree(node.left, node.val, True)
            right = validTree(node.right, node.val, False)

            return res and left and right
        
        ans = validTree(root, float('inf'), True)

        return ans
            
            