n, m = 5, 4
graph = [[0,1,0,1,1],
         [1,0,1,1,0],
         [0,1,0,0,0],
         [1,1,0,0,0],
         [1,0,0,0,0]]
trip = [2, 3, 4, 3]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    p_of_a = find_parent(parent, a)
    p_of_b = find_parent(parent, b)
    if a < b:
        parent[p_of_b] = p_of_a
    else:
        parent[p_of_a] = p_of_b

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

result = True
for i in range(m-1):
    if find_parent(parent, trip[i]) != find_parent(parent, trip[i + 1]):
        result = False

print(result)