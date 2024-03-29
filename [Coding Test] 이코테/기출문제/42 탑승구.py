g = 4
p = 3
docking = [4, 1, 1]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (g + 1)
for i in range(1, g + 1):
    parent[i] = i

result = 0
for i in range(p):
    data = find_parent(parent, docking[i])
    if data == 0:
        break
    union_parent(parent, data, data - 1)
    result += 1

print(result)