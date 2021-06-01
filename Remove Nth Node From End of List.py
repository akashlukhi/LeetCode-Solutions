# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        temp = head
        if length == 1 and n == 1:
            return None
        if length == n:
            return head.next
        for i in range(1, length - n):
            temp = temp.next
        print(temp.val)
        if temp.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        return head
