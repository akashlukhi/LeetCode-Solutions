# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        if k == 0:
            return head
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        if length == 1:
            return head
        k = k % length
        if k == 0:
            return head
        i = length - k - 1
        temp = head
        while i > 0:
            i -= 1
            temp = temp.next
        t = temp.next
        temp.next = None
        temphead = head
        head = t
        while t.next:
            t = t.next
        t.next = temphead
        return head
        