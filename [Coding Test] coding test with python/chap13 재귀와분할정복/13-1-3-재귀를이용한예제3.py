# https://www.acmicpc.net/problem/17070

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 0, 1, 2 = 가로, 세로, 대각선
ans = 0
def recursive(r, c, shape):
    global ans
    if r > n - 1 or c > n - 1:
        return
    if r == n - 1 and c == n - 1:
        ans += 1
    # 가로
    if data[r][c + 1] == 0 and (shape == 0 or shape == 2):
        recursive(r, c + 1, 0)
    # 세로
    if data[r + 1][c] == 0 and (shape == 1 and shape == 2):
        recursive(r + 1, c, 1)
    # 대각선
    if data[r + 1][c] == 0 and data[r][c + 1] == 0 and data[r + 1][c + 1] == 0:
        recursive(r + 1, c + 1, 2)

recursive(0, 1, 0)
print(ans)