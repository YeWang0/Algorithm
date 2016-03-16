# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def sortedArrayToBST(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: TreeNode
#         """
#         n=len(nums)
nums=[1,2,3,4,5,6,7,8]
n=len(nums)


def sort(l,r):
    if l<=r:
        m=(l+r)//2
        head=TreeNode(nums[m])

        head.left=sort(l,m-1)
        head.right=sort(m+1,r)

        return head

def show(head):
    if head:
        show(head.left)
        print head.val
        show(head.right)
head=sort(0,n-1)
show(head)
