# 역순 연결 리스트
## 반복 구조로 뒤집기
def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next , prev
        prev, node = node, next
    
    return prev