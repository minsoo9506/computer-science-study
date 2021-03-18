#  상위 k 빈도 요소
nums = [1,1,1,2,2,3]
k = 2

import collections
import heapq
from typing import List

def topK(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk

def topK2(nums: List[int], k: int) -> List[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

print(topK2(nums, k))

fruits = ['a','b','c']
print(list(zip(fruits,fruits)))