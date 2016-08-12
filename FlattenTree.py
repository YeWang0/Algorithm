# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        def convert(node):
            # if node:
            #     print node.val
            # else:
            #     print 'NULL'
            if not node.left and not node.right:
                return node
            elif not node.left:
                return convert(node.right)
            elif not node.right:
                node.right=node.left
                node.left=None
                return convert(node.right)
            else:
                end=convert(node.left)

                right=node.right
                node.right=node.left
                node.left=None
                if end:
                    print end.val,right.val
                    end.right=right
                    return convert(right)
        convert(root)
            