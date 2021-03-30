# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pointer = head
        l = []

        while pointer:
            l.append(pointer.val)
            pointer = pointer.next
        
        l.sort()

        pointer = head
        for i in range(len(l)):
            pointer.val = l[i]
            pointer = pointer.next
        
        return head