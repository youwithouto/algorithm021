"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        result = []
        self.doPreorder(root, result)
        return result

    def doPreorder(self, root: Node, result: List[int]):
        if root is None:
            return
        result.append(root.val)
        for child in root.children:
            self.doPreorder(child, result)
