# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp = []
        while head is not None:
            temp.append(head.val)
            head = head.next
        
        while len(temp) >= 2:
            if temp.pop(0) != temp.pop():
                return False
        
        return True
        
