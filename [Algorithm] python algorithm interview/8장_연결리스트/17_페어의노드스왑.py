# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = root = ListNode(None)
        node = head  # 코드 읽을 때, 편의를 위해
        prev.next = node
        while node and node.next:
            b = node.next
            node.next = b.next
            b.next = node

            prev.next = b

            node = node.next
            prev = prev.next.next
        return root.next
