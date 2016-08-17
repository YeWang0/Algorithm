# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        def getLength(node):
            i=0
            while node!=None:
                node=node.next
                i+=1
            return i
        # n=getLength(head)
        # print n
        def findmidNode(node):
            p=node
            if node:
                # print node.val
                l=getLength(node)
                print l
                n=(l-1)//2
                if l==1:
                    return node.val,None,None
                elif l==2:
                    return node.val,None,node.next
                else:
                    while n>1:
                        node=node.next
                        n-=1
                    if node.next:
                        value=node.next.val
                        temp=node.next.next
                        node.next=None
                        # print value,p.val,temp.val
                        return value,p,temp
                    else:
                        print 'oh no!'
            else:
                print 'null'
                return None,None,None
        node=head
        Tree=TreeNode(0)
        f=Tree
        def createTree(node,Tree):
            value,left,right=findmidNode(node)
            # print value,left.val,right.val
            if value!=None:
                Tree.val=value
                # print '...'
                if left:
                    Tree.left=TreeNode(0)
                    print left.val
                    print
                    createTree(left,Tree.left)
                if right:
                    Tree.right=TreeNode(0)
                    createTree(right,Tree.right)

        createTree(node,Tree)
        return f



