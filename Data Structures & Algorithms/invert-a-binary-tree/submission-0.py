# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(curr):
            es = curr.left
            curr.left = curr.right
            curr.right = es

        def invert(root):
            if not root:
                return
            if root.left or root.right:
                swap(root)

            invert(root.left)
            invert(root.right)

        invert(root)

        return root


        
