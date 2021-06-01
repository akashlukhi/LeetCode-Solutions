# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        num2 = ''
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        ans = str(int(num1) + int(num2))
        i = len(ans) - 1
        head = ListNode(ans[i])
        i -= 1
        t = head
        while i >= 0:
            temp = ListNode(ans[i])
            i -= 1
            t.next = temp
            t = t.next
        return head
