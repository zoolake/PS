# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1)
        # 역순으로 변경
        def reverseList(head: ListNode) -> ListNode:
            current, previous = head, None
            while current:
                next, current.next = current.next, previous
                previous, current = current, next
            return previous

        # 연결리스트->리스트
        def toList(node: ListNode) -> list:
            l = []
            while node:
                l.append(node.val)
                node = node.next
            print(l)
            return l
        
        # 리스트->연결리스트
        def toLinkedList(l: list) -> ListNode:
            link = ListNode()
            for idx, val in enumerate(l):
                if idx==0:
                    link.val = val
                else:
                    node = link
                    while node.next != None:
                        node = node.next
                    node.next = ListNode(val)
            return link

        a = toList(reverseList(l1))
        b = toList(reverseList(l2))

        answer = int(''.join(str(val) for val in a)) + int(''.join(str(val) for val in b))
        return reverseList(toLinkedList(str(answer)))