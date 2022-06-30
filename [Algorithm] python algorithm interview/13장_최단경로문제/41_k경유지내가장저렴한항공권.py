# https://leetcode.com/problems/cheapest-flights-within-k-stops/


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        graph = collections.defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((cost, end))

        dist = [1e9] * n
        dist[0] = 0

        q = [(0, src, k)]

        while q:
            cost, node, k = heapq.heappop(q)
            if node == dst:
                return cost
            if k >= 0:
                for x, y in graph[node]:
                    if dist[y] > cost + x:
                        dist[y] = cost + x
                        heapq.heappush(q, (cost + x, y, k - 1))

        return -1
