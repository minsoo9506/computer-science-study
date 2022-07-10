# https://leetcode.com/problems/minimum-height-trees/


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        # 양방향 트리
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 리프노드를 삭제해가는 방법
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            new_leaves = []
            n -= len(leaves)
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
