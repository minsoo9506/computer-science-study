# 두수의 덧셈
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    def toList(self, node: ListNode) -> ListNode:
        list = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
         
        return self.toReversedLinkedList(str(resultStr))