# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        nowroots = [root]
        while nowroots:
            ans.insert(0, [subroot.val for subroot in nowroots])
            nextroots = []
            for subroot in nowroots:
                if subroot.left:
                    nextroots.append(subroot.left)
                if subroot.right:
                    nextroots.append(subroot.right)
            nowroots = nextroots
        return ans
