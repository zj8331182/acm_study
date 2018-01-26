"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class SolNodeution:
    """
    @param: root: the root of tree
    @return: the max node
    """

    def maxNode(self, root):
        if root is None:
            return None
        return searchInNodes(root, root)


def searchInNodes(root, max_):
    """
    中序遍历
    :rtype:TreeNode
    """
    if root.val > max_.val:
        max_ = root
    if root.left is not None:
        max_ = searchInNodes(root.left, max_)
    if root.right is not None:
        max_ = searchInNodes(root.right, max_)
    return max_
