# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 재귀
        # def recursive(current: ListNode, previous: ListNode=None):
        #     if not current:
        #         return previous
            
        #     next, current.next = current.next, previous
        #     return recursive(next, current)
        # return recursive(head)
        # 반복
        current, previous = head, None
        
        while current:
            next, current.next = current.next, previous
            previous, current = current, next
        
        return previous