# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=[]
        # top=head
        pre=ListNode(0)
        pre.next=head
        copy=pre
        forward=head
        while pre!=None and forward!=None:
            value=forward.val
            if not current:
                current=[value]
                forward=forward.next
            elif value in current:
                current.append(value)
                forward=forward.next
            else:
                if len(current)>1:
                    for i in current:
                        pre.next=pre.next.next
                    forward=forward.next
                    current=[value]
                    # remove dup
                else:
                    current=[value]
                    pre=pre.next
                    forward=forward.next
        if len(current)>1:
            # print current
            for i in current:
                pre.next=pre.next.next
        return copy.next
                    