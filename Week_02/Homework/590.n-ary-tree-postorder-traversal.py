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
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.doPostorder(root, result)
        return result

    def doPostorder(self, root: 'Node', result):
        if root is None:
            return
        for child in root.children:
            self.doPostorder(child, result)
        result.append(root.val)
