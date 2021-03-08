# 페어의 노드 스왑

def swapPairs(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next
    return root.next