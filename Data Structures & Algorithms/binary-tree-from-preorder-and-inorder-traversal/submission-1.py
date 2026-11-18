# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTreeRecur(self, mp, preorder, preIndex, left, right) -> Optional[TreeNode]:
        if left > right:
            return None

        rootVal = preorder[preIndex[0]]
        preIndex[0] += 1

        root = TreeNode(rootVal)

        index = mp[rootVal]

        # Recursively create the left and right subtree.
        root.left = self.buildTreeRecur(mp, preorder, preIndex, left, index - 1)
        root.right = self.buildTreeRecur(mp, preorder, preIndex, index + 1, right)

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {value: idx for idx, value in enumerate(inorder)}
        preIndex = [0]
    
        return self.buildTreeRecur(mp, preorder, preIndex, 0, len(inorder) - 1)