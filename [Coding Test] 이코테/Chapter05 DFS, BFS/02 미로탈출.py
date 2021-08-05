n, m = 5, 6
input_data = [[1,0,1,0,1,0]
              [1,1,1,1,1,1],
              [0,0,0,0,0,1],
              [1,1,1,1,1,1],
              [1,1,1,1,1,1]]

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    while queue:
        r, c = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 전체 공간을 벗어난 경우 무시
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            # 벽인 경우 무시
            if input_data[nr][nc] == 0:
                continue
            # 해당 위치를 처음 방문하는 경우 최단 거리 업데이트
            if input_data[nr][nc] == 1:
                input_data[nr][nc] += input_data[r][c]
                queue.append((nr, nc))
    return input_data[n-1][m-1]

print(bfs(0,0))