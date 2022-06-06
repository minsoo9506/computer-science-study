# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = self._addLinkedList(l1, l2)
        result = self._makeReversedLinkedList(result)

        return result

    def _addLinkedList(self, l1, l2):
        a, b = 0, 0
        i = 0
        while l1 or l2:
            if l1:
                a += 10**i * l1.val
                l1 = l1.next
            if l2:
                b += 10**i * l2.val
                l2 = l2.next
            i += 1
        sum_val = str(a + b)
        return sum_val

    def _makeReversedLinkedList(self, sum_val):
        prev = None
        for s in sum_val:
            node = ListNode(s)
            node.next = prev
            prev = node
        return node
