# https://www.acmicpc.net/problem/15684

n, m, h = map(int, input().split())
data = [[0] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    r, c = map(int, input().split())
    data[r][c] = 1
    data[r][c + 1] = 2

# 가로선을 넣을 수 있는 위치 (왼쪽기준)
line = []
for i in range(1, h + 1):
    for j in range(1, n):
        if data[i][j] == 0 and data[i][j + 1] == 0:
            line.append((i, j))

def move(c):
    r = 1
    while r <= h:
        if data[r][c] == 1: # 1이면 오른쪽으로 이동
            c += 1
        if data[r][c] == 2: # 2이면 왼쪽으로 이동
            c -= 1
        r += 1
    return c

def check():
    for i in range(1, n):
        result = move(i)
        if result != i:
            return False
    return True

ans = -1

for i in range(len(line)):
    r1, c1 = line[i]
    if data[r1][c1] != 0 or data[r1][c1 + 1] != 0:
        continue
    data[r1][c1] = 1
    data[r1][c1 + 1] = 2
    if check():
        if ans == -1 or ans > 1:
            ans = 1
    for j in range(i + 1, len(line)):
        r2, c2 = line[j]
        if data[r2][c2] != 0 and data[r2][c2 + 1] != 0:
            continue
        data[r2][c2] = 1
        data[r2][c2 + 1] = 2
        if check():
            if ans == -1 or ans > 2:
                ans = 2
        for k in range(j + 1, len(line)):
            r3, c3 = line[k]
            if data[r3][c3] != 0 and data[r3][c3 + 1] != 0:
                continue
            data[r3][c3] = 1
            data[r3][c3 + 1] = 2
            if check():
                if ans == -1 or ans > 3:
                    ans = 3
            data[r3][c3] = 0
            data[r3][c3 + 1] = 0
        data[r2][c2] = 0
        data[r2][c2 + 1] = 0
    data[r1][c1] = 0
    data[r1][c1 + 1] = 0

print(ans)