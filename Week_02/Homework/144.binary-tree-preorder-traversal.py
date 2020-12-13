# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.doPreorderTraversal(root, result)
        return result

    def doPreorderTraversal(self, root: TreeNode, result: List[int]):
        if root is None:
            return
        result.append(root.val)
        self.doPreorderTraversal(root.left, result)
        self.doPreorderTraversal(root.right, result)
