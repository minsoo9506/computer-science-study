# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        # 나중에 return을 쉽게 하기 위해 root를 갖고 있자
        root = before = ListNode(None)
        root.next = head
        # before, end 지정
        for _ in range(left - 1):
            before = before.next
        end = before.next

        # 노드 뒤집기
        for _ in range(right - left):
            tmp, before.next, end.next = before.next, end.next, end.next.next
            before.next.next = tmp
        return root.next
