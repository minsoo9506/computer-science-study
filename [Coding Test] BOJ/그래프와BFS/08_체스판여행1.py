# https://www.acmicpc.net/problem/16959
# 원래 문제에서는 1부터 시작하게 되어있지만 0부터 시작이라고 가정
n = map(int, input().split())
data = []
for _ in range(n):
    for _ in range(n):
        data.append(list(map(int, input().split())))

# (r,c,num,말)
check = [[[[-1] * 3 for _ in range(n * n)] for _ in range(n)] for _ in range(n)]

# 말의 종류
# 0:나이트, 1:룩, 2:비숍
moves0 = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
moves1 = [(-1,0),(1,0),(0,-1),(0,1)]
moves2 = [(-1,-1),(-1,1),(1,-1),(1,1)]

from collections import deque

q = deque()
for r in range(n):
    for c in range(n):
        if data[r][c] == 1:
            for i in range(3):
                q.append((r,c,1,i))
                check[r][c][0][i] = 0
ans = -1
while q:
    r, c, num, p = q.popleft()
    if num == n * n - 1:
        if ans == -1 or ans > check[r][c][num][p]:
            ans = check[r][c][num][p]
    # 말 교체
    for i in range(3):
        if p == i:
            continue
        if check[r][c][num][i] == -1:
            check[r][c][num][i] = check[r][c][num][p] + 1
            q.append((r,c,num,i))
            
    # 이동
    if p == 0:
        for i in range(8):
            nr, nc = r + moves0[i], c + moves0[i]
            if 0 <= nr < n and 0 <= nc < n:
                next_num = num
                if data[nr][nc] == num + 1:
                    next_num = num + 1
                if check[nr][nc][next_num][p] == -1:
                    check[nr][nc][next_num][p] = check[nr][nc][num][p] + 1
                    q.append((nr, nr, next_num, p))

    elif p == 1:
        for i in range(4):
            l = 1
            while True:
                nr, nc = r + moves1[i] * l, c + moves1[i] * l
                if 0 <= nr < n and 0 <= nc < n:
                    next_num = num
                    if data[nr][nc] == num + 1:
                        next_num = num + 1
                    if check[nr][nc][next_num][p] == -1:
                        check[nr][nc][next_num][p] = check[nr][nc][num][p] + 1
                        q.append((nr, nr, next_num, p))
                else:
                    break
                l += 1
    else:
        for i in range(4):
            l = 1
            while True:
                nr, nc = r + moves2[i] * l, c + moves2[i] * l
                if 0 <= nr < n and 0 <= nc < n:
                    next_num = num
                    if data[nr][nc] == num + 1:
                        next_num = num + 1
                    if check[nr][nc][next_num][p] == -1:
                        check[nr][nc][next_num][p] = check[nr][nc][num][p] + 1
                        q.append((nr, nr, next_num, p))
                else:
                    break
                l += 1
print(ans)