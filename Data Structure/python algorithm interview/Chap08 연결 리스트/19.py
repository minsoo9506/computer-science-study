def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    # 예외처리
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head
    # start, end 지정
    for _ in range(m - 1):
        start = start.next
    end = start.next

    for  _ in range(m - n):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    
    return root.next