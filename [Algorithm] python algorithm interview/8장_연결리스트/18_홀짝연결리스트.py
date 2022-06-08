# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외처리
        if head is None:
            return None

        odd_node = head
        even_node = head.next
        even_head = head.next

        while even_node and even_node.next:
            odd_node.next, even_node.next = odd_node.next.next, even_node.next.next
            odd_node, even_node = odd_node.next, even_node.next

        # odd_node의 마지막을 even_head에 연결
        odd_node.next = even_head
        return head
