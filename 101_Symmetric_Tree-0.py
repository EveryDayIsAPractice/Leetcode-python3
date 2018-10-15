# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        if root.left==None and root.right==None:
            return True
        elif root.left==None or root.right==None:
            return False
        elif root.right.val != root.left.val:
            return False
        out = TreeNode(0)
        ins = TreeNode(0)
        out.right = root.right.right
        out.left  = root.left.left
        ins.right = root.right.left
        ins.left  = root.left.right
        if self.isSymmetric(out):
            if self.isSymmetric(ins):
                return True
            else:
                return False
        else:
            return False

