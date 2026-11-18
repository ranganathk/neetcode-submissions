# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (not p and not q):
            return True
        if (not p or not q):
            return False
        if (p.val != q.val):
            return False

        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)

        return isLeftSame and isRightSame

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        res = self.isSameTree(root, subRoot)

        if not root:
            return False

        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        
