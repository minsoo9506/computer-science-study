# https://leetcode.com/problems/course-schedule/

import collections

# 순환구조가 생기는지 확인하는 것
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(x):
            if x in traced:
                return False

            if x in visited:
                return True

            traced.add(x)

            for y in graph[x]:
                if not dfs(y):
                    return False

            traced.remove(x)
            visited.add(x)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
