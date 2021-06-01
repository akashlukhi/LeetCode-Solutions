# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while (1 < len(lists)):
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            if l1 == None:
                lists.append(l2)
                continue
            if l2 == None:
                lists.append(l1)
                continue
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
            lists.append(head)

        if len(lists) == 1:
            return lists[0]
        else:
            return
