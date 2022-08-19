# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))  # O(logn)

        result = []
        for _ in range(k):
            (dist, x, y) = heapq.heappop(heap)  # O(logn)
            result.append((x, y))
        return result
