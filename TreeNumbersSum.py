# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        global result
        result=0
        def cal(list):
            r=0
            for i in list:
               r=r*10+i
            return r
        def search(node,list):
            global result
            if not node.left and not node.right:
                temp=list[:]
                temp.append(node.val)
                # print temp
                result+=cal(temp)
            else:
                temp=list[:]
                temp.append(node.val)
                if node.left:
                    search(node.left,temp)
                if node.right:
                    search(node.right,temp)
        search(root,[])
        return result

        