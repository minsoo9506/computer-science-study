# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 오름차순
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = parent = ListNode(0)
        while head:
            # head 보다 큰 값을 만나는 경우 위치 바꾸는 전략
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # cur 포인터를 필요한 경우만 되돌아가도록
            if head and cur.val > head.val:
                cur = parent

        return parent.next
