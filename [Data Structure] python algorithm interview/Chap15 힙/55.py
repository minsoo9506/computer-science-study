# 배열의 k번재 큰 요소
unsorted_data = [3,2,3,1,2,4,5,5,6]
k = 4

from types import List
import heapq

def findKthLargest(nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n) # python에서 최소힙이라 - 붙여서 최대힙처럼 이용
    for _ in range(k - 1):
        heapq.heappop(heap)
    return heapq.heappop(heap)

def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify(nums) # 바로 최소힙 만들어준다

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

def findKthLargest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1] # nsmallest도 있다