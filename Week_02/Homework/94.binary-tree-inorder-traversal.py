# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.doInorderTraversal(root, result)
        return result

    def doInorderTraversal(self, root: TreeNode, result: List[int]):
        if root is None:
            return result
        self.doInorderTraversal(root.left, result)
        result.append(root.val)
        self.doInorderTraversal(root.right, result)
