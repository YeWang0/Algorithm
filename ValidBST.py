# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result=[]
        def binary(node):
            if not node:
                return
            binary(node.left)
            result.append(node.val)
            binary(node.right)
        binary(root)
        # print result
        for i in xrange(1,len(result)):
            if result[i]<=result[i-1]:
                return False
        return True
