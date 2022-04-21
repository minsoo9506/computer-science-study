# https://www.acmicpc.net/problem/1520
# 내리막길

n, m = map(int, input())
data = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def dp_func(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    if r == n - 1 and c == m - 1:
        return 1
    # 방문했으면 0으로 표시
    dp[r][c] = 0
    for i in range(0, 4):
        nr = r + moves[i][0]
        nc = c + moves[i][1]
        if 0 <= nr < n and 0 <= nc < m and data[r][c] > data[nr][nc]:
            dp[r][c] += dp_func(nr, nc)
    return dp[r][c]

print(dp_func(0,0))