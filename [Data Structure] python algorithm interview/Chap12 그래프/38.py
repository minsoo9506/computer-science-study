# 일정 재구성
import collections

def find(tickets):
    graph = collections.defaultdict(list)
    # 사전순 거꾸로 넣는다
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JKL')
    return route[::-1]