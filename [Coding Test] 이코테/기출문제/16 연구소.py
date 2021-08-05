col , row = 7, 7
data = [[2,1,0,0,1,1,0],
        [1,0,1,0,1,2,0],
        [0,1,1,0,1,0,0],
        [0,1,0,0,0,1,0],
        [0,0,0,0,0,1,1],
        [0,1,0,0,0,0,0],
        [0,1,0,0,0,0,0]]

import copy
tmp = copy.deepcopy(data)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
    # bfs로 근처에 virus가 퍼지는 경우 만들기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >=0 and nx < row and ny < col:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(row):
        for j in range(col):
            if tmp[i][j] == 0:
                score += 1
    return score

result = 0

def dfs(count):
    global result
    if count == 3:
        for i in range(row):
            for j in range(col):
                tmp[i][j] = data[i][j]
        for i in range(row):
            for j in range(col):
                if tmp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    # 벽 3개 만드는 과정
    for i in range(row):
        for j in range(col):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)