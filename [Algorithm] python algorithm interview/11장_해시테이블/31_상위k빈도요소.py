# https://leetcode.com/problems/top-k-frequent-elements/


import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # 갯수 세기
        counter = collections.Counter(nums)
        # 최대힙 만들기
        c_heap = []
        for c in counter.keys():
            heapq.heappush(c_heap, (-counter[c], c))
        # 결과
        result = []
        for _ in range(k):
            result.append(heapq.heappop(c_heap)[1])
        return result


# 근데 Counter의 .most_common() 함수를 이용하는게 더 편하긴 하다
