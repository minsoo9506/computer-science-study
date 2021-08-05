n = 3
L , R = 5, 10
data = [[10, 15, 20],
        [20, 30, 25],
        [40, 22, 10]]

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

from collections import deque
def process(r, c, index):
    united = []
    united.append((r, c))

    q = deque()
    q.append((r, c))
    union[r][c] = index # 현재 연합의 번호 할당
    total = data[r][c]
    count = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc <n and union[nr][nc] == -1:
                if L <= abs(data[nr][nc] - data[r][c]) <= R:
                    q.append((nr, nc))
                    union[nr][nc] = index
                    total += data[nr][nc]
                    count += 1
                    united.append((nr, nc))
    for i, j in united:
        data[i][j] = total // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
            break
    total_count += 1

print(total_count)
