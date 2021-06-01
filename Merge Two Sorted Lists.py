# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            ans = ListNode(l1.val)
            l1 = l1.next
        else:
            ans = ListNode(l2.val)
            l2 = l2.next
        head = ans
        while l1 and l2:
            if(l1.val > l2.val):
                temp = ListNode(l2.val)
                l2 = l2.next
            else:
                temp = ListNode(l1.val)
                l1 = l1.next
            ans.next = temp
            ans = ans.next
        while l1:
            temp = ListNode(l1.val)
            l1 = l1.next
            ans.next = temp
            ans = ans.next
        while l2:
            temp = ListNode(l2.val)
            l2 = l2.next
            ans.next = temp
            ans = ans.next
        return head
