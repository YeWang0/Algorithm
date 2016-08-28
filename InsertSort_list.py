# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre=ListNode(0)
        pre.next=head
        start=head.next
        head.next=None
        # return pre
        while start!=None:
            p=pre
            next=start.next
            flag=False
            while p.next:
                if start.val<=p.next.val:
                    temp=p.next
                    p.next=start
                    start.next=temp
                    flag=True
                    break
                else:
                    p=p.next
            if not flag:
                p.next=start
                start.next=None
            start=next
        return pre.next
                    