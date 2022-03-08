# https://www.acmicpc.net/problem/17070

n = 3
data = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# 0: 가로, 1: 대각선, 2:세로

ans = 0
def solution(r, c, direction):
    global ans
    if r == (n - 1) and c == (n - 1):
        return 1
    if direction == 0:
        if c + 1 < n and data[r][c + 1] == 0:
            ans += solution(r, c + 1, 0)
        if r + 1 < n and c + 1 < n and data[r + 1][c] == 0 and data[r][c + 1] == 0 and data[r + 1][c + 1] == 0:
            ans += solution(r + 1, c + 1, 1)
    elif direction == 1:
        if c + 1 < n and data[r][c + 1] == 0:
            ans += solution(r, c + 1, 0)
        if r + 1 < n and data[r + 1][c] == 0:
            ans += solution(r + 1, c, 2)
        if r + 1 < n and c + 1 < n and data[r + 1][c + 1] == 0:
            ans += solution(r + 1, c + 1, 1)
    else:
        if r + 1 < n and data[r + 1][c] == 0:
            ans += solution(r + 1, c, 2)
        if r + 1 < n and c + 1 < n and data[r + 1][c] == 0 and data[r][c + 1] == 0 and data[r + 1][c + 1] == 0:
            ans += solution(r + 1, c + 1, 1)

    return ans

print(solution(0, 1, 0))