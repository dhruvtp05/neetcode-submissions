# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        placeholder1 = root.left
        placeholder2 = root.right

        root.left = placeholder2
        root.right = placeholder1

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root