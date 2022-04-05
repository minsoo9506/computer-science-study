# https://www.acmicpc.net/problem/3190

n, k = map(int, input().split())

board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
times = {}
for _ in range(l):
    x, c = input().split()
    times[x] = c

moves = [(-1,0),(0,1),(1,0),(0,-1)]
board[1][1] = 2

from collections import deque
snake = deque()
snake.append((1,1))

# 위 오른쪽 아래 왼쪽: 0 1 2 3
# D: + 1, L: - 1 -> 그리고 3+1 -> 0, 0-1 -> 3 으로 만들기
def direction_change(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

r, c = 1, 1
direction = 1
time = 0
while True:
    nr, nc = r + moves[direction], c + moves[direction]
    if 1 <= nr <= n and 1 <= nc <= n and board[nr][nc] != 2:
        if board[nr][nc] != 1:
            del_r, del_c = snake.popleft()
            board[del_r][del_c] == 0
        snake.append((nr, nc))
        board[nr][nc] == 2
        time += 1
        for t in times.keys():
            if time == t:
                direction_change(direction, times[time])
    else:
        break