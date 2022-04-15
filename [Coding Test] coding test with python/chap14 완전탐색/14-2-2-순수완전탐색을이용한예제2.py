# 체스판 다시 칠하기
# https://wwww.acmicpc.net/problem/1018

n, m = map(int, input().split())
data = [input() for _ in range(n)]

# r, c 가 8*8의 맨 처음 위치
result = int(1e9)
for r in range(n - 7):
    for c in range(m - 7):
        a = 0 
        b = 0
        for i in range(r, r + 8):
            for j in range(c, c + 8):
                if (i + j) % 2 == 0:
                    if data[i][j] != 'W': a += 1
                    if data[i][j] != 'B': b += 1
                else:
                    if data[i][j] != 'B': a += 1
                    if data[i][j] != 'W': b += 1
        result = min(result, a, b)
print(result)