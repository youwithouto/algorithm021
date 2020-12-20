# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        stack = []
        current = root.left
        pLeft, qLeft = False, False
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if current == p:
                pLeft = True
            if current == q:
                qLeft = True

            if pLeft and qLeft:
                break

            current = current.right

        if pLeft and qLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        elif not pLeft and not qLeft:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
