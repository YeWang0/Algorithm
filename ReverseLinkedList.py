# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        pre=ListNode(0)
        pre.next=head
        def reverse(m,n):
            p=pre
            q=pre
            for i in xrange(m-1):
                p=p.next
            for j in xrange(n-1):
                q=q.next
            # print p.val,q.val
            temp=p.next
            p.next=q.next
            q.next=temp
            temp=p.next.next
            p.next.next=q.next.next
            q.next.next=temp
        while m<n:
            reverse(m,n)
            m+=1
            n-=1
        return pre.next
        