# https://leetcode.com/problems/palindrome-linked-list/

# 러너 활용
def solution(head):
    rev = None
    slow = fast = head

    # 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next  # fast는 두칸씩
        rev, rev.next, slow = slow, rev, slow.next
    if fast:  # 길이가 짝홀수냐에 따라 slow
        slow = slow.next

    # 팰린드롬 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
