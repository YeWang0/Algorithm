# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        q=head
        if q==None or q.next==None:
            return None
        while p and q:
            p=p.next
            if q.next:
                q=q.next.next
            else:
                return None
            if p==q:
                break
        if p==None or q==None:
            return None
        while head != q:
            head = head.next
            q = q.next
        return head
        # slow, fast = head, head
        # while True:
        #     if fast == None or fast.next == None: return None
        #     slow = slow.next; fast = fast.next.next
        #     if slow == fast: break
        # while head != fast:
        #     head = head.next; fast = fast.next
        # return head