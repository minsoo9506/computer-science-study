# 펠린드롬 연결 리스트
# deque
import collections
def isPalindrome(head: ListNode) -> bool:
    q = collections.deque()
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True

# 러너를 이용
def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev