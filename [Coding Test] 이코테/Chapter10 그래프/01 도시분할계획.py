v, e = 7, 12
# edges = (cost, a, b)
edges = [(1,2,3),(1,3,2),(3,2,1),
(2,5,2),(3,4,4),(7,3,6),
(5,1,5),(1,6,2),(6,4,1),
(6,5,3),(4,5,3),(6,7,4)]

parents = [0] * (v + 1)
for i in range(1, v + 1):
    parents[i] = i

edges.sort()

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a_p = find_parent(parent, a)
    b_p = find_parent(parent, b)
    
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

last = 0
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union(parents, a, b)
        result += cost
        last = cost

print(result - last)