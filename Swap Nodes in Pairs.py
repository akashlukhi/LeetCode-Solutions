# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            arr = []
            temp = head
            while temp:
                arr.append(temp.val)
                temp = temp.next
            for i in range(0, len(arr) - 1, 2):
                t = arr[i]
                arr[i] = arr[i + 1]
                arr[i+1] = t
            temp = ListNode(arr[0])
            head = temp
            for i in range(1, len(arr)):
                t = ListNode(arr[i])
                temp.next = t
                temp = temp.next
            return head
