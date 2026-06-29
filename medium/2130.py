# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        fast = slow.next
        slow.next = None
        prev=None
        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        maximum=0
        while prev:
            v1=prev.val
            v2=head.val
            inmax=v1+v2
            maximum=max(maximum, inmax)
            prev = prev.next
            head = head.next
        return maximum

        