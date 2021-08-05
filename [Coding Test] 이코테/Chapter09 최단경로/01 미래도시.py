num_nodes = 10
x = 3 # 중간에 거칠 node
k = 6 # 최종 도착 node

for k in range(1, num_nodes+1):
    for j in range(1, num_nodes+1):
        for i in range(1, num_nodes+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][x] + graph[x][k]