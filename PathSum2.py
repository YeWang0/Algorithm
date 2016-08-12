# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result=[]
        if not root:
            return result
        def search(node,pre,value):
            # print pre,value,node.val
            if not node.left and not node.right:
                if value+node.val==sum:
                    print 'yes'
                    pre.append(node.val)
                    result.append(pre[:])
                    pre.pop()
            # if value+node.val>sum:
            #     return
            if node.left:
                pre.append(node.val)
                search(node.left,pre,value+node.val)
                pre.pop()
            if node.right:
                pre.append(node.val)
                search(node.right,pre,value+node.val)
                pre.pop()
        search(root,[],0)
        return result