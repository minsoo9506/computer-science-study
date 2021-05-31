# 해시맵 디자인
# 개별 체이닝
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = next

import collections

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # index에 노드가 없는 경우
        # defaultdict는 index가 없으면 바로 생성하기에
        # if self.table[index] is None: 이렇게 하면 무조건 True
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        # 노드가 있는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                return
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # index의 첫번째 노드일 때 삭제처리
        p = self.table[index]
        if p.key == key:
            # if self.table[index].value is None: 이부분이 에러나지 않도록하기 위해
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next