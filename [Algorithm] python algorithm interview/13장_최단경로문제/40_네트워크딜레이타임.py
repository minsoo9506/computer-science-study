# https://leetcode.com/problems/network-delay-time/


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = collections.defaultdict(int)
        # 우선순위큐 이용
        Q = [(0, k)]

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    cost = time + w
                    heapq.heappush(Q, (cost, v))

        if len(dist) == n:
            return max(dist.values())
        return -1
