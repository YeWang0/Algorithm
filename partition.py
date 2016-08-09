# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        pre=ListNode(0)
        pre.next=head
        cp=pre
        if head.val<x:
            right=head.next
            while right!=None and right.val<x :
                right=right.next
            if right==None:
                return cp.next
            left=head
            while left.next!=None and left.next.val<x:
                left=left.next
        else:
            right=head
            while right.next!=None and right.next.val>=x :
                right=right.next
            if right==None:
                return cp.next
            left=pre
        while right.next:
            value=right.next.val
            if value<x:
                temp=right.next
                right.next=right.next.next
                temp.next=left.next
                left.next=temp

                left=left.next
            else:
                right=right.next
        return cp.next
        