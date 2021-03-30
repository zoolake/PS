# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = start = ListNode()
        while head:
            # 더 작은 값을 만날때 까지 포인터를 옮겨줌
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next

            # 필요한 경우에만 cur 포인터가 start로 되돌아가게끔 처리 (약 10배 정도 빨라짐)
            if head and cur.val > head.val:
                cur = start

        return start.next
